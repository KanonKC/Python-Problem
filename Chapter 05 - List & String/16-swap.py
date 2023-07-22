container = [i for i in input("Enter a list: ").split()]

while True:
    x,y = [int(i) for i in input("Swap index: ").split()]
    if x == -1 and y == -1:
        break
    
    tmp = container[x]
    container[x] = container[y]
    container[y] = tmp

    for i in container:
        print(i, end=' ')