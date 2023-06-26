from random import random,randint

def createTestcase(testcase):
    print('::elab:begintest hint="-"')
    for i in range(len(testcase)):
        print(testcase[i])
    print("::elab:endtest")

universe = ""
setA = ""
for i in range(1,1000+1):

    universe += str(i) + " "

for i in range(250):
    setA += str(randint(1,1000)) + " "

print(universe)
print(setA)