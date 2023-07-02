text = input("Enter text: ").lower()
collection = {}

for letter in text:
    if letter not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
        continue
    if letter in collection:
        collection[letter] += 1
    else:
        collection[letter] = 1

for letter in collection:
    print(f"{letter}: {collection[letter]}")