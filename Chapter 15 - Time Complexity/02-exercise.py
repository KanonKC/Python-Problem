def func2(n:int) -> int:
    count = 0
    i = 0
    j = 0
    while i < n:
        j = -i
        while j < i:
            count += 1
            j += 2
        i += 1
    return count

def func3(n:int) -> int:
    count = 0
    i = 1
    j = 0
    while i < n:
        j = -i
        while j < n:
            count += 1
            j += i
        i += 1
    return count

def func4(a:int,b:int) -> int:
    if b == 0:
        return 1
    if b % 2 == 1:
        y = func4(a,(b-1)//2)
        return a*y*y
    else:
        y = func4(a,b//2)
        return y*y
    
def doSomething(n:int) -> None:
    for i in range(1,n):
        if i <= 10:
            print("Hello #1")
        elif i % 10 == 1:
            j = i
            total = 0
            while total <= n:
                print("Hello #2")
                total += j
                j += 1
        else:
            j = i
            while j <= n:
                print("Hello #3")
                j += j*2