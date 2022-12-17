def oneDifferent(a,b):
    point = 1
    result = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            if point == 1:
                result += "?"
                point = 0
            else:
                return -1
        else:
            result += a[i]
    return result

text = input("Text: ")
substring = input("Substring: ")
lsub = len(substring)

splitted_text = text.split(substring)
if len(splitted_text) == 1:
    i = 0
    while i < len(text)-lsub+1:
        sliced = text[i:i+lsub]
        diff = oneDifferent(sliced,substring)
        if diff != -1:
            text = f"{text[:i]}[{diff}]{text[i+lsub:]}"
            i += 2 + lsub
        else:
            i += 1
    print(text)
else:
    joined_text = f"[{substring}]".join(splitted_text)
    print(joined_text)