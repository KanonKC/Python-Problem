text = input("Enter a word: ")

if text == text[::-1]:
    print(f"{text} is a Palindrome")
else:
    print(f"{text} is not a Palindrome")