first = 0
second = -1
while True:
    x = int(input())
    if x == 0:
        break
    if x > first:
        second = first
        first = x
    elif x > second:
        second = x
print(second)