from math import sqrt

n = int(input())
max_length = 0
for a in range(1,n):
    for b in range(1,n):
        res = sqrt(a**2 + b**2)
        if a+b+res == n and int(res) == res and res > max_length:
            max_length = int(res)

print(max_length)