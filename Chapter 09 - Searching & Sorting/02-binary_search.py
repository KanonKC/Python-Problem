collection = [int(i) for i in input().split()]
target = int(input())

left = 0
right = len(collection) - 1

while left <= right:
    mid = (left + right) // 2
    print(f"Current item: {collection[mid]} at index #{mid}")
    if collection[mid] == target:
        print("Found!")
        break
    elif collection[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Not Found!")