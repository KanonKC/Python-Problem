n = int(input("N: "))

if n == 1 or (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0) and (n != 2 and n != 3 and n != 5 and n != 7):
    print(f"{n} is not a Prime Number")
else:
    print(f"{n} is a Prime Number")