from random import random,randint

count = int(input("How many testcase: "))
line = int(input("How many line for each testcase: "))
number_type = input("Type of input(int/float/all): ")
number_range = [int(i) for i in input("Range: ").split()]

for i in range(count):
    print('::elab:begintest hint="-"')
    for j in range(line):
        roll = random()
        if number_type == "float" or (number_type == "all" and roll > 0.5):
            print(round(randint(number_range[0],number_range[1]) + random(),3))
        else:
            print(randint(number_range[0],number_range[1]))
    print("::elab:endtest")