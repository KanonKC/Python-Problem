def createSet(label):
    numbers = input(label).split()
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

def printSet(set):
    for item in set:
        print(item, end=" ")

def complement(set,universe):
    result = []
    for n in universe:
        if n not in set:
            result.append(n)
    return result

u = createSet("Enter Universe: ")
a = createSet("Enter Set A: ")

printSet(complement(a,u))

