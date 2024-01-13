N = int(input())
food = [int(i) for i in input().split()]
diff = [0 for i in range(N)]
maxEat = 0

for i in range(N):
    res = (food[i]-i) % N
    diff[res] += 1
    maxEat = max(maxEat,diff[res])

print(maxEat)