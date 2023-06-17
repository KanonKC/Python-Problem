numbers = input("Enter integers: ").split()
numbers = [int(i) for i in numbers if '.' not in i]

print(sum(numbers))