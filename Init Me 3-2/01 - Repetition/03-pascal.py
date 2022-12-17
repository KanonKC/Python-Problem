def fac(n):
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

def combination(n,r):
    return fac(n)//(fac(r)*fac(n-r))

n = int(input("Input: "))

for i in range(n):
    for j in range(i+1):
        print(combination(i,j),end=" ")
    print()