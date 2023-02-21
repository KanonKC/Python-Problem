binary = input("Enter binary: ")

decimal = 0
for i in range(len(binary)):
    decimal += int(binary[-i-1]) * (2**i)

print(decimal)