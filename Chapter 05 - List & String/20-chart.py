data = [int(i) for i in input().split()]

for i in range(len(data)-1,-1,-1):
    for j in range(i):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]
    