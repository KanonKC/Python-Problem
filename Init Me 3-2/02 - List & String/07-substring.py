text = input("Text: ")
substring = input("Substring: ")

splitted_text = text.split(substring)
if len(splitted_text) == 1:
    print("Not found")
else:
    joined_text = f"[{substring}]".join(splitted_text)
    print(joined_text)