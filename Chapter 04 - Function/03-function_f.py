def f(x):
    if x >= 5 and x <= 25:
        print("Betw",x)
        return 3*x - 5
    else:
        return 5

x = int(input())
print(f(x),f(2*x)) # 5 + 29 