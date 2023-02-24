value = input("Enter value: ")
precision = int(input("Precision: ")) + 1

pre_position = value.index('.') + precision

target = int(value[pre_position])
next = int(value[pre_position - 1])
result = value[:pre_position - 1]

if target <= 4 or (target == 5 and next % 2 == 0):
    result += str(next)
elif target >= 6 or (target == 5 and next % 2 != 0):
    result += str(next+1)

print(result)