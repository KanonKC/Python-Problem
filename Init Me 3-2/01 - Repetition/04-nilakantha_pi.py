def pieCal(n):
    return ((-1)**n)*4/(((n-1)*2)*(((n-1)*2)+1)*(((n-1)*2)+2))

x = int(input("n: "))
i = 1
PI = 0

while i <= x:
    if i == 1:
        PI += 3
    else:
        PI += pieCal(i)
    i+=1

print(f"PI: {PI:.10f}")