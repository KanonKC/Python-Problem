m = int(input("m: "))
y = int(input("y: "))
y-=543
if m == 2:
    if (y%4==0 and y%100!=0) or y%400==0:
        print("29")
    else:
        print("28")
elif m in [4,6,9,11]:
    print("30")
else:
    print("31")