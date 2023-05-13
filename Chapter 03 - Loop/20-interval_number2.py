startNumber = int(input("Start: "))
endNumber = int(input("End: "))

if endNumber > startNumber:
    for i in range(startNumber,endNumber+1):
        print(i,end=" ")
else:
    for i in range(startNumber,endNumber-1,-1):
        print(i,end=" ")