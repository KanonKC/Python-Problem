[n,k,t] = [int(i) for i in input().split()]
count = 0

holder = 1
initial = True

while ((holder != 1 or initial) and holder != t):
    initial = False
    count += 1
    holder = (holder + k) % n

if (holder == t):
    count += 1

print(count)