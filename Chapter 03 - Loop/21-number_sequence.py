N = int(input("N: "))

print("Sequence 1")
for i in range(N+1):
    print(i,end=" ")

print()
print("Sequence 2")
for i in range(N,-1,-1):
    print(i,end=" ")

print()
print("Sequence 3")
for i in range(N):
    print(i*2,end=" ")

print()
print("Sequence 4")
for i in range(N//2,N+1):
    print(i,end=" ")

print()
print("Sequence 5")
for i in range(N):
    print(i**2,end=" ")

print()
print("Sequence 6")
for i in range(N):
    print((-1)**i*(2*i+1),end=" ")