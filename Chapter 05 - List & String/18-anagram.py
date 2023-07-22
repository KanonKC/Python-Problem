text1 = input("Enter text 1: ")
text2 = input("Enter text 2: ")

if sorted(text1) == sorted(text2):
    print("Anagram!")
else:
    print("Not anagram!")