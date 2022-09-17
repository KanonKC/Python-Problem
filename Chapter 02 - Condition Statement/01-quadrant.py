x = float(input("x: "))
y = float(input("y: "))

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    if y > 0:
        print("Positive Y-Axis")
    else:
        print("Negative Y-Axis")
elif y == 0:
    if x > 0:
        print("Positive X-Axis")
    else:
        print("Negative X-Axis")
elif x > 0:
    if y > 0:
        print("Quadrant 1")
    else:
        print("Quadrant 4")
else:
    if y > 0:
        print("Quadrant 2")
    else:
        print("Quadrant 3")