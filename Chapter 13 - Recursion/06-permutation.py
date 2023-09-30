def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def permutation(arr, start, end):
    if start == end:
        print(arr)
    else:
        for i in range(start, end):
            swap(arr, start, i)
            permutation(arr, start + 1, end)
            swap(arr, start, i)

arr = [i for i in input("Enter a words: ").split()]
permutation(arr, 0, len(arr))