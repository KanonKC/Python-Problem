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

def intersection(set1,set2):
    result = []
    for n in set1:
        if n in set2:
            result.append(n)
    for n in set2:
        if n in set1 and n not in result:
            result.append(n)
    return result

a = createSet("Enter Set A: ")
b = createSet("Enter Set B: ")

printSet(intersection(a,b))