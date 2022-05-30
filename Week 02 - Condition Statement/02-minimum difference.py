x = int(input("x: "))
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

minimum_value = a
minimum = abs(x-a)

if abs(x-b) < minimum:
    minimum_value = b
    minimum = abs(x-b)
if abs(x-c) < minimum:
    minimum_value = c
    minimum = abs(x-c)

print(f"{minimum_value} is closest to {x}")