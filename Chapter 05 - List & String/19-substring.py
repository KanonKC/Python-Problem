text = input("Enter text: ")
substring = input("Enter substring: ")

result = ""

i = 0
while i < len(text):
    if i+len(substring) > len(text):
        result += text[i:]
        break
    elif text[i:i+len(substring)] == substring:
        result += f"[{text[i:i+len(substring)]}]"
        i += len(substring)
    else:
        result += text[i]
        i += 1

print(result)