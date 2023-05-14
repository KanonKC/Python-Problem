count = 0

while True:
    x = int(input())
    
    if x == 0:
        break
    elif x > 0:
        count += 1

print(f"Found {count} positive integer(s)")