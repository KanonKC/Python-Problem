def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n = int(input()) + 1

while not (isPrime(n) and isPrime(n+2)):
    n += 1

print(f"{n}, {n+2}")