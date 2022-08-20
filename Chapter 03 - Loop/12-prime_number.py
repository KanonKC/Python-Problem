from math import sqrt

n = int(input("n: "))

for i in range(2,int(sqrt(n))+1):
    if n % i == 0:
        print(f"{n} is not a Prime Number")
        break
else:
    if n == 1:
        print("1 is not a Prime Number")
    else:
        print(f"{n} is a Prime Number")