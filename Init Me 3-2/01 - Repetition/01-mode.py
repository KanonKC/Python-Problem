data = [int(i) for i in input("Enter list of numbers: ").split()]
store = [0 for _ in range(max(data)+1)]

for i in data:
    store[i] += 1

max_value = max(store)
for i in data:
    if store[i] == max_value:
        store[i] += 1
        print(i)