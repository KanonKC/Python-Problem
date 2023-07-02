text = input("Enter text: ").lower().split()
collection = {}

for word in text:
    stripedWord = word.strip(".,!?")
    if stripedWord in collection:
        collection[stripedWord] += 1
    else:
        collection[stripedWord] = 1

for word in collection:
    print(f"{word}: {collection[word]}")