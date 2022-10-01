s = input("Input text: ")
n = int(input("N: "))

for i in range(len(s)):
    if i % n == 0 and i != 0:
        print()
    print(s[i],end="")
