number = input("Enter number: ")

start = 0

while number[start] in "0.":
    start += 1

significant = len(number[start:])

if '.' in number[start:]:
    significant -= 1

print(f"Significant: {significant}")