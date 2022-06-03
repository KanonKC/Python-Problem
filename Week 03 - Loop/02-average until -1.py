total = 0
count = 0

while True:
    x = float(input())
    if x == -1:
        break
    total += x
    count += 1

if count == 0:
    print("No Data")
else:
    print(total/count)