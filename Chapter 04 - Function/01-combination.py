def fac(n):
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

n = int(input())
r = int(input())

print(fac(n)//(fac(r)*fac(n-r)))