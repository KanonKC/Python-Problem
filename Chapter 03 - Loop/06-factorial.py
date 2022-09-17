n = int(input("n: "))

res = 1
for i in range(1,n+1):
    res *= i

if n == 0:
    print(1)
else:
    print(res)