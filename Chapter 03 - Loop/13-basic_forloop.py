n = int(input())
if n == 1:
    for i in range(10):
        print(i,end=" ")
elif n == 2:
    for i in range(5,11):
        print(i,end=" ")
elif n == 3:
    for i in range(2,16,2):
        print(i,end=" ")
elif n == 4:
    for i in range(9,-1,-1):
        print(i,end=" ")
elif n == 5:
    for i in range(1,13):
        print(i**2,end=" ")
elif n == 6:
    for i in range(11):
        print((2*i+1)*((-1)**i),end=" ")