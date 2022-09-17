n = int(input())
side = input()

if side == 'left':
    for i in range(1,n+1):
        print(f"{' '*(n-i)}{'#'*i}")
else:
    for i in range(1,n+1):
        print('#'*i)