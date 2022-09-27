text = input("Enter a word: ")

for i in range(len(text)//2):
    if text[i] != text[-i-1]:
        print(f"{text} is not a Palindrome")
        break
else:
    print(f"{text} is a Palindrome")