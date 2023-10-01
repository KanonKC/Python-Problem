import regex as re

code = """
def mysum(a, b):
    asdwadw
    asdwadawd
    if askdjwkjd:
        asldkwldk
    else:
        kewllelkwl
    return 5
"""

code = ";".join([i.strip() for i in code.split("\n") if i != ""])

x = re.search("def mysum(.*):.*return.*mysum(.*)", code)

# Print code with raw string format
print([code])
print(bool(x))