value = input("Enter value: ")
sig = int(input("Enter significant number: "))

if '.' in value:
    len_value = len(value) - 1
else:
    len_value = len(value)
    value += '.'

while len_value < sig:
    value += '0'

print(value)