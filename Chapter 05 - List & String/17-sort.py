container = [int(i) for i in input("Enter a list: ").split()]

container.sort(reverse=True)

for i in container:
    print(i, end=' ')