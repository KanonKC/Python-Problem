max_number = 0
while True:
    x = int(input())
    if x == 0:
        break
    elif x > max_number:
        max_number = x
print(max_number)