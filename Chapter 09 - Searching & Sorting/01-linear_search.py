collection = [int(i) for i in input().split()]
target = int(input())

for i in range(len(collection)):
    print(f"Current item: {collection[i]} at index #{i}")
    if collection[i] == target:
        print("Found!")
        break
else:
    print("Not Found!")