a = int(input())
b = int(input())
c = int(input())

maximum_value = a

if b > maximum_value:
    maximum_value = b
if c > maximum_value:
    maximum_value = c

print(maximum_value)