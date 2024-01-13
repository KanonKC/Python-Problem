n = int(input())

count = 0

# dish[i] -> จานลำดับที่ i มีขนาดเท่าไหร่
dish = []

# counter[i] -> จานไซส์ i มีกี่จาน
counter = [0 for i in range(301)]

for i in range(n):
    dish.append(int(input()))

for i in range(n):
    counter[dish[i]] += 1
    count = max(count,counter[dish[i]])

print(count)