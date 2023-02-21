def f(x):
    if x >= 5 and x <= 25:
        return 3*x - 5
    else:
        return 5

x = int(input("x: "))
print(f(x) + f(2*x))