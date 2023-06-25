numbers = input("Enter set: ").split()
result = []

for n in numbers:
    if n not in result:
        result.append(n)

for item in result:
    print(item, end=" ")