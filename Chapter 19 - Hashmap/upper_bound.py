# N = int(input())
vector = [1,3,5,7,9,12,16,19,25,36,65,90]

def upper_bound(vector, target):
    left = 0
    right = len(vector)-1
    while left < right:
        mid = (left+right)//2
        if vector[mid] <= target:
            left = mid+1
        else:
            right = mid
    return left

print(vector[upper_bound(vector,65)])

