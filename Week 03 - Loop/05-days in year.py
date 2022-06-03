d = int(input("D: "))
m = int(input("M: "))
y = int(input("Y: "))
y -= 543
total = d
for i in range(1,m):
    if i == 2:
        if (y%4 == 0 and y%100 != 0) or y%400==0:
            total += 29
        else:
            total += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        total += 30
    else:
        total += 31

print(total)