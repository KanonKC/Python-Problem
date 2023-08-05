def removeSpaces(text):
    return text.replace(" ", "")

text1 = input("Enter text 1: ").lower()
text2 = input("Enter text 2: ").lower()

if sorted(removeSpaces(text1)) == sorted(removeSpaces(text2)):
    print("Anagram!")
else:
    print("Not anagram!")