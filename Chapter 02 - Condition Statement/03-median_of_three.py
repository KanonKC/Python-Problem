print("Enter 3 Numbers:")
a = int(input("#1: "))
b = int(input("#2: "))
c = int(input("#3: "))

if (a >= b and a <= c) or (a >= c and a <= b):
    print(f"Median is {a}")
elif (b >= a and b <= c) or (b >= c and b <= a):
    print(f"Median is {b}")
else:
    print(f"Median is {c}")