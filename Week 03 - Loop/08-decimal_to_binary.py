n = int(input())
binary = ""

if n == 0:
    binary = "0"
while n != 0:
    binary = f"{n%2}{binary}"
    n //= 2
    
print(binary)