text = input("Input text: ")
col = int(input("N: "))

result = ["" for i in range(col)]

for i in range(len(text)):
    result[i%col] += text[i]

for i in result:
    print(i)