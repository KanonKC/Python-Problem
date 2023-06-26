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
    print()

def complement(set,universe):
    result = []
    for n in universe:
        if n not in set:
            result.append(n)
    return result

def minus(set1,set2):
    result = []
    for n in set1:
        if n not in set2:
            result.append(n)
    return result

def union(set1,set2):
    result = []
    for n in set1:
        if n not in result:
            result.append(n)
    for n in set2:
        if n not in result:
            result.append(n)
    return result

def intersection(set1,set2):
    result = []
    for n in set1:
        if n in set2:
            result.append(n)
    for n in set2:
        if n in set1 and n not in result:
            result.append(n)
    return result

u = createSet("Enter Universe: ")
a = createSet("Enter Set A: ")
b = createSet("Enter Set B: ")
c = createSet("Enter Set C: ")

while True:
    x = input("Enter equation: ")

    if x == "":
        break

    if x[0] == "A":
        set1 = a
    elif x[0] == "B":
        set1 = b
    elif x[0] == "C":
        set1 = c
    elif x[0] == "U":
        set1 = u

    if len(x) == 3:
        if x[2] == "A":
            set2 = a
        elif x[2] == "B":
            set2 = b
        elif x[2] == "C":
            set2 = c
        elif x[2] == "U":
            set2 = u

    if x[1] == "+":
        printSet(union(set1,set2))
    elif x[1] == "*":
        printSet(intersection(set1,set2))
    elif x[1] == "-":
        printSet(minus(set1,set2))
    elif x[1] == "'":
        printSet(complement(set1,u))