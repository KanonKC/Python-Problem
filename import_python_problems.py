#!/usr/bin/env python3
"""Import the Elab-style problems of the Python-Problem repository into Verdale.

For every `Chapter XX - .../Problems/*.md` it:
  1. turns the Elab Markdown into a Verdale statement (HTML -> Markdown/KaTeX),
  2. takes the `::elab:begincode` block as the primary reference solution,
  3. takes every `::elab:begintest` block as the stdin of one testcase and gets the
     expected output by running the reference solution locally,
  4. creates the problem (draft, Python only), its solution and its testcases in
     Core through the public API. With --publish it also publishes each problem.

Only the standard library is used. Nothing is written without --space and a session.

Dry run (parses, runs every solution, prints a report, touches no server):
    python3 import_python_problems.py --dry-run

Real run (get the `vd_session` cookie value from the browser's dev tools after signing in):
    VERDALE_SESSION=<cookie value> python3 import_python_problems.py --space my-space

Problems that cannot be imported are skipped and listed at the end: Go problems (Verdale
judges C, C++ and Python), and problems whose solution fails on every test (for example the
File Handling chapter, which opens data files the judge sandbox does not have).
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_SOURCE_DIRECTORY = Path.home() / "Documents" / "Python-Problem"

# Limits from Verdale-core-service/src/constants/limits.ts
MAX_TESTS_PER_PROBLEM = 100
MAX_TEST_FILE_BYTES = 8 * 1024 * 1024
MAX_SAMPLE_FILE_BYTES = 64 * 1024
MAX_SAMPLES = 10
MAX_TITLE_LENGTH = 200
MAX_STATEMENT_LENGTH = 100_000
MAX_SOURCE_BYTES = 65_536
MAX_SLUG_LENGTH = 64

SOLUTION_TIMEOUT_SECONDS = 10
# Core allows 300 requests per minute per client address; stay below it.
MINIMUM_SECONDS_BETWEEN_REQUESTS = 0.25
MAX_RATE_LIMIT_RETRIES = 6


# --------------------------------------------------------------------------- parsing


@dataclass
class ElabProblem:
    markdown_path: Path
    slug: str
    title: str
    statement: str
    solution_source: str
    test_inputs: list[str]
    example_count: int


@dataclass
class ImportReport:
    imported: list[str] = field(default_factory=list)
    skipped: list[tuple[str, str]] = field(default_factory=list)
    warnings: list[tuple[str, str]] = field(default_factory=list)


def build_slug(markdown_path: Path) -> str:
    chapter_match = re.search(r"Chapter\s+(\d+)", str(markdown_path))
    chapter_prefix = f"ch{int(chapter_match.group(1)):02d}" if chapter_match else "misc"
    file_stem = re.sub(r"[^a-z0-9_-]+", "-", markdown_path.stem.lower()).strip("-_")
    return f"{chapter_prefix}-{file_stem}"[:MAX_SLUG_LENGTH].rstrip("-_")


def convert_statement(raw_statement: str) -> str:
    """Elab Markdown contains HTML and MathJax; Verdale renders Markdown + KaTeX only."""
    statement = raw_statement

    statement = re.sub(
        r'<script\s+type="math/tex[^"]*"[^>]*>(.*?)</script>',
        lambda match: f"${match.group(1).strip()}$",
        statement,
        flags=re.DOTALL,
    )
    statement = re.sub(r"<!--.*?-->", "", statement, flags=re.DOTALL)
    statement = re.sub(
        r"\\\[(.*?)\\\]", lambda match: f"$${match.group(1).strip()}$$", statement, flags=re.DOTALL
    )
    statement = re.sub(
        r"\\\((.*?)\\\)", lambda match: f"${match.group(1).strip()}$", statement, flags=re.DOTALL
    )
    statement = re.sub(r"<u>(.*?)</u>", r"**\1**", statement, flags=re.DOTALL)

    def preformatted_to_fence(match: re.Match[str]) -> str:
        block_text = html.unescape(match.group(1)).strip("\n")
        return f"\n```text\n{block_text}\n```\n"

    statement = re.sub(r"<pre[^>]*>(.*?)</pre>", preformatted_to_fence, statement, flags=re.DOTALL)
    statement = re.sub(r"\n{3,}", "\n\n", statement)
    return statement.strip() + "\n"


def parse_problem(markdown_path: Path) -> ElabProblem | str:
    """Returns the problem, or a string explaining why it cannot be imported."""
    text = markdown_path.read_text(encoding="utf-8").replace("\r\n", "\n")

    title_match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    if not title_match:
        return "no `# Title` line"
    title = title_match.group(1)[:MAX_TITLE_LENGTH]

    code_match = re.search(r"^::elab:begincode[^\n]*\n(.*?)^::elab:endcode", text, re.DOTALL | re.MULTILINE)
    if not code_match:
        return "no ::elab:begincode block (no reference solution)"
    solution_source = code_match.group(1)
    if "package main" in solution_source:
        return "Go problem (Verdale judges C, C++ and Python)"
    if len(solution_source.encode("utf-8")) > MAX_SOURCE_BYTES:
        return "reference solution is over 64 KiB"

    test_inputs = [
        match.group(1)
        for match in re.finditer(
            r"^::elab:begintest[^\n]*\n(.*?)^::elab:endtest", text, re.DOTALL | re.MULTILINE
        )
    ]
    if not test_inputs:
        return "no ::elab:begintest blocks"

    statement_raw = text[: code_match.start()]
    statement_raw = statement_raw[title_match.end() :]
    statement = convert_statement(statement_raw)
    if len(statement) > MAX_STATEMENT_LENGTH:
        return "statement is over 100 000 characters"

    return ElabProblem(
        markdown_path=markdown_path,
        slug=build_slug(markdown_path),
        title=title,
        statement=statement,
        solution_source=solution_source,
        test_inputs=test_inputs,
        example_count=len(re.findall(r"^##\s+Example", statement_raw, flags=re.MULTILINE)),
    )


# ------------------------------------------------------------------ expected outputs


def run_reference_solution(solution_source: str, stdin_text: str) -> tuple[str | None, str]:
    """Returns (stdout, "") on success or (None, reason) on failure."""
    with tempfile.TemporaryDirectory() as working_directory:
        solution_path = Path(working_directory) / "main.py"
        solution_path.write_text(solution_source, encoding="utf-8")
        try:
            completed = subprocess.run(
                [sys.executable, str(solution_path)],
                input=stdin_text.encode("utf-8"),
                capture_output=True,
                cwd=working_directory,
                timeout=SOLUTION_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return None, f"timed out after {SOLUTION_TIMEOUT_SECONDS}s"
    if completed.returncode != 0:
        last_error_line = (completed.stderr.decode("utf-8", "replace").strip().splitlines() or ["?"])[-1]
        return None, f"exit code {completed.returncode}: {last_error_line}"
    try:
        return completed.stdout.decode("utf-8"), ""
    except UnicodeDecodeError:
        return None, "output is not valid UTF-8"


@dataclass
class GeneratedTest:
    input_text: str
    output_text: str
    is_sample: bool


def generate_tests(problem: ElabProblem, report: ImportReport) -> list[GeneratedTest] | str:
    generated: list[GeneratedTest] = []
    failure_reasons: list[str] = []
    for test_number, input_text in enumerate(problem.test_inputs, start=1):
        output_text, failure_reason = run_reference_solution(problem.solution_source, input_text)
        if output_text is None:
            failure_reasons.append(f"test {test_number}: {failure_reason}")
            continue
        too_large = max(len(input_text), len(output_text)) > MAX_TEST_FILE_BYTES
        if too_large:
            failure_reasons.append(f"test {test_number}: file is over 8 MiB")
            continue
        generated.append(GeneratedTest(input_text, output_text, is_sample=False))

    if not generated:
        return "reference solution fails on every test (" + failure_reasons[0] + ")"
    if failure_reasons:
        report.warnings.append((problem.slug, f"{len(failure_reasons)} test(s) dropped: " + "; ".join(failure_reasons[:3])))
    if len(generated) > MAX_TESTS_PER_PROBLEM:
        report.warnings.append((problem.slug, f"kept the first {MAX_TESTS_PER_PROBLEM} of {len(generated)} tests"))
        generated = generated[:MAX_TESTS_PER_PROBLEM]

    # The statement's "## Example N" sections are the first tests in these files, so the
    # same number of leading tests become samples (at least one: the publish gate needs it).
    sample_count = min(max(1, problem.example_count), MAX_SAMPLES)
    for generated_test in generated[:sample_count]:
        small_enough = max(len(generated_test.input_text), len(generated_test.output_text)) <= MAX_SAMPLE_FILE_BYTES
        generated_test.is_sample = small_enough
    return generated


# ------------------------------------------------------------------------- API client


class VerdaleApiError(Exception):
    def __init__(self, status: int, body: str, request_description: str):
        super().__init__(f"{request_description} -> HTTP {status}: {body[:400]}")
        self.status = status
        self.body = body


class VerdaleClient:
    def __init__(self, api_base_url: str, origin: str, session_token: str):
        self.api_base_url = api_base_url.rstrip("/")
        self.origin = origin
        self.session_token = session_token
        self._last_request_at = 0.0

    def request(self, method: str, path: str, *, json_body=None, multipart: tuple[bytes, str] | None = None):
        if json_body is not None:
            body_bytes = json.dumps(json_body).encode("utf-8")
            content_type = "application/json"
        elif multipart is not None:
            body_bytes, content_type = multipart
        else:
            body_bytes, content_type = None, None

        description = f"{method} {path}"
        for attempt in range(MAX_RATE_LIMIT_RETRIES):
            waited = time.monotonic() - self._last_request_at
            if waited < MINIMUM_SECONDS_BETWEEN_REQUESTS:
                time.sleep(MINIMUM_SECONDS_BETWEEN_REQUESTS - waited)
            self._last_request_at = time.monotonic()

            http_request = urllib.request.Request(
                f"{self.api_base_url}{path}", data=body_bytes, method=method
            )
            http_request.add_header("Cookie", f"vd_session={self.session_token}")
            http_request.add_header("Origin", self.origin)
            http_request.add_header("Accept", "application/json")
            if content_type:
                http_request.add_header("Content-Type", content_type)
            try:
                with urllib.request.urlopen(http_request, timeout=60) as response:
                    response_text = response.read().decode("utf-8")
                    return json.loads(response_text) if response_text else None
            except urllib.error.HTTPError as error:
                response_text = error.read().decode("utf-8", "replace")
                if error.code == 429:
                    retry_after = error.headers.get("Retry-After")
                    time.sleep(float(retry_after) if retry_after and retry_after.isdigit() else 10 * (attempt + 1))
                    continue
                raise VerdaleApiError(error.code, response_text, description) from None
            except urllib.error.URLError as error:
                raise VerdaleApiError(0, str(error.reason), description) from None
        raise VerdaleApiError(429, "still rate limited after retries", description)


def build_multipart_test_body(generated_test: GeneratedTest) -> tuple[bytes, str]:
    boundary = f"----verdale{uuid.uuid4().hex}"
    chunks: list[bytes] = []

    def add_file(field_name: str, file_name: str, content: str) -> None:
        chunks.append(
            (
                f"--{boundary}\r\nContent-Disposition: form-data; name=\"{field_name}\"; "
                f"filename=\"{file_name}\"\r\nContent-Type: text/plain\r\n\r\n"
            ).encode()
        )
        chunks.append(content.encode("utf-8"))
        chunks.append(b"\r\n")

    add_file("input", "input.txt", generated_test.input_text)
    add_file("output", "output.txt", generated_test.output_text)
    chunks.append(
        (
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"is_sample\"\r\n\r\n"
            f"{'true' if generated_test.is_sample else 'false'}\r\n--{boundary}--\r\n"
        ).encode()
    )
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def upload_problem(
    client: VerdaleClient,
    space_slug: str,
    problem: ElabProblem,
    generated_tests: list[GeneratedTest],
    publish: bool,
) -> str:
    """Returns "created" or "exists". On any failure after creation, deletes the draft."""
    problems_path = f"/api/v1/spaces/{space_slug}/problems"
    problem_path = f"{problems_path}/{problem.slug}"

    try:
        client.request(
            "POST",
            problems_path,
            json_body={
                "slug": problem.slug,
                "title": problem.title,
                "statement": problem.statement,
                "allowed_languages": ["python"],
            },
        )
    except VerdaleApiError as error:
        if error.status == 409:
            return "exists"
        raise

    try:
        client.request(
            "POST",
            f"{problem_path}/solutions",
            json_body={"language": "python", "source": problem.solution_source, "is_primary": True},
        )
        for generated_test in generated_tests:
            client.request("POST", f"{problem_path}/tests", multipart=build_multipart_test_body(generated_test))
        if publish:
            client.request("POST", f"{problem_path}/publish", json_body={})
    except VerdaleApiError:
        # Do not leave a half-filled draft behind: a re-run would skip it as "exists".
        try:
            client.request("DELETE", problem_path)
        except VerdaleApiError:
            pass
        raise
    return "created"


# ------------------------------------------------------------------------------ main


def find_problem_files(source_directory: Path, only_substring: str | None) -> list[Path]:
    markdown_files = sorted(source_directory.glob("Chapter *"))
    markdown_files = [path for chapter in markdown_files for path in sorted((chapter / "Problems").glob("*.md"))]
    if only_substring:
        markdown_files = [path for path in markdown_files if only_substring.lower() in str(path).lower()]
    return markdown_files


def main() -> int:
    argument_parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    argument_parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE_DIRECTORY, help="Python-Problem checkout")
    argument_parser.add_argument("--space", help="slug of the Verdale Space to import into")
    argument_parser.add_argument("--api", default="http://localhost:8080", help="Core base URL (default: %(default)s)")
    argument_parser.add_argument("--origin", default="http://localhost:3000", help="web app origin Core expects (FRONTEND_ORIGIN)")
    argument_parser.add_argument("--session", default=os.environ.get("VERDALE_SESSION"), help="vd_session cookie value (or env VERDALE_SESSION)")
    argument_parser.add_argument("--publish", action="store_true", help="also publish each imported problem (default: leave drafts)")
    argument_parser.add_argument("--only", help="import only files whose path contains this text, e.g. 'Chapter 05'")
    argument_parser.add_argument("--dry-run", action="store_true", help="parse and run solutions only; contact no server")
    arguments = argument_parser.parse_args()

    if not arguments.dry_run and not (arguments.space and arguments.session):
        argument_parser.error("--space and a session (--session or VERDALE_SESSION) are required unless --dry-run")
    if not arguments.source.is_dir():
        argument_parser.error(f"source directory not found: {arguments.source}")

    client = None if arguments.dry_run else VerdaleClient(arguments.api, arguments.origin, arguments.session)
    report = ImportReport()
    markdown_files = find_problem_files(arguments.source, arguments.only)
    print(f"{len(markdown_files)} problem file(s) found in {arguments.source}\n")

    for position, markdown_path in enumerate(markdown_files, start=1):
        label = f"{markdown_path.parent.parent.name}/{markdown_path.name}"
        parsed = parse_problem(markdown_path)
        if isinstance(parsed, str):
            report.skipped.append((label, parsed))
            print(f"[{position}/{len(markdown_files)}] SKIP   {label}: {parsed}")
            continue

        generated = generate_tests(parsed, report)
        if isinstance(generated, str):
            report.skipped.append((label, generated))
            print(f"[{position}/{len(markdown_files)}] SKIP   {label}: {generated}")
            continue

        sample_total = sum(1 for generated_test in generated if generated_test.is_sample)
        if client is None:
            report.imported.append(parsed.slug)
            print(f"[{position}/{len(markdown_files)}] OK     {parsed.slug}  ({len(generated)} tests, {sample_total} sample)")
            continue

        try:
            outcome = upload_problem(client, arguments.space, parsed, generated, arguments.publish)
        except VerdaleApiError as error:
            report.skipped.append((label, f"upload failed: {error}"))
            print(f"[{position}/{len(markdown_files)}] FAIL   {label}: {error}")
            if error.status in (401, 403, 0):
                print("Stopping: the session, the Origin or the server is wrong; fix that and re-run.")
                break
            continue
        if outcome == "exists":
            report.skipped.append((label, f"slug {parsed.slug} already exists in the Space"))
            print(f"[{position}/{len(markdown_files)}] EXISTS {parsed.slug}")
        else:
            report.imported.append(parsed.slug)
            print(f"[{position}/{len(markdown_files)}] CREATED {parsed.slug}  ({len(generated)} tests, {sample_total} sample)")

    print(f"\n{'Would import' if arguments.dry_run else 'Imported'}: {len(report.imported)}   Skipped: {len(report.skipped)}")
    if report.skipped:
        print("\nSkipped:")
        for label, reason in report.skipped:
            print(f"  - {label}: {reason}")
    if report.warnings:
        print("\nWarnings:")
        for slug, warning in report.warnings:
            print(f"  - {slug}: {warning}")
    return 0 if not any("upload failed" in reason for _, reason in report.skipped) else 1


if __name__ == "__main__":
    sys.exit(main())
