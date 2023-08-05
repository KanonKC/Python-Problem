def printList(list):
    for i in list:
        print(i, end=' ')
    print()

container = [int(i) for i in input("Enter a list: ").split()]

container.sort(reverse=True)

printList(container)