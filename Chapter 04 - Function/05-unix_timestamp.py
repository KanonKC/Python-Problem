def isLeap(y):
    return (y%4 == 0 and y%100 != 0) or y%400==0

d = int(input("Date: "))
m = int(input("Month: "))
y = int(input("Year: "))

h = int(input("Hour: "))
mn = int(input("Minute: "))
s = int(input("Second: "))

total = d
for i in range(1,m):
    if i == 2:
        if isLeap(y):
            total += 29
        else:
            total += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        total += 30
    else:
        total += 31

for i in range(1970,y):
    if isLeap(i):
        total += 366
    else:
        total += 365

total = ((total-1) * 86400) + (h*3600) + (mn*60) + s

print(total)