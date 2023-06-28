words = input("Words: ").split(' ')
result = []

for word in words:
    if word not in result:
        result.append(word)

for r in result:
    print(r)