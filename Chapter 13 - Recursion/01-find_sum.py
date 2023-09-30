n = [int(i) for i in input("Enter numbers: ").split()]

def findSum(n):
    if len(n) == 0:
        return 0
    return n[0] + findSum(n[1:])

print(findSum(n))