def f(x):
    if x >= 5 and x <= 25:
        return 3*x - 5
    else:
        return 5

def g(x,y):
    if x > 0:
        return x + y
    elif x < 0:
        return 5*x*y
    else:
        return 1

x = int(input("x: "))
y = int(input("y: "))

print(f(y)*g(y,x))