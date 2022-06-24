n = int(input())

side = (n//2) + 1

for i in range(1,side):
    print(f"{'#'*i}{' '*(n-(2*i))}{'#'*i}")
print("#"*n)
for i in range(side-1,0,-1):
    print(f"{'#'*i}{' '*(n-(2*i))}{'#'*i}")