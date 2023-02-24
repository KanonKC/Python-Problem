words = []
max_len = 0

while True:
    text = input()

    if text == "":
        break

    words.append(text)
    max_len = max(max_len,len(text))

for word in words:
    print(f"{' '*(max_len-len(word))}{word}")