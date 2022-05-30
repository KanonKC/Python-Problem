from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)

print(f"x1 = {x1:.3f} ,x2 = {x2:.3f}")