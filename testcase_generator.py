from random import random,randint

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# print("Generating Sample...")
# CUSTOMIZE = [i for i in range(1,10000) if isPrime(i)]

count = int(input("How many testcase: "))
input_type = [i for i in input("Type of input(int/float/all/str/custom) for each line: ").split()]

testcase = []

for i in range(len(input_type)):
    if input_type[i] == "str":
        testcase.append([i for i in input("Enter String's Sample Space: ").split()])
    elif input_type[i] in ["int","float"]:
        testcase.append([int(i) for i in input("Range: ").split()])        
        

for i in range(count):
    print('::elab:begintest hint="-"')
    for j in range(len(input_type)):
        roll = random()
        if input_type[j] == "str":
            print(testcase[j][randint(0,len(testcase[j])-1)])
        elif input_type[j] == "float" or (input_type[j] == "all" and roll > 0.5):
            print(round(randint(testcase[j][0],testcase[j][1]) + random(),3))
        elif input_type[j] == "int" or (input_type[j] == "all" and roll <= 0.5):
            print(randint(testcase[j][0],testcase[j][1]))
        else:
            print(CUSTOMIZE[randint(0,len(CUSTOMIZE)-1)])
    print("::elab:endtest")