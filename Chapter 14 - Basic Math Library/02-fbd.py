from math import sin, cos, radians

f = float(input("Enter force: "))
a = float(input("Enter angle: "))

print(f"Horizontal component: {f*cos(radians(a)):.2f}")
print(f"Vertical component: {f*sin(radians(a)):.2f}")