from generator import TestcaseGenerator
from random import randint,random

class ProblemTestcase(TestcaseGenerator):

    CUSTOM = True

    def customGenerator(self) -> None:
        for t in range(9):

            if t < 2:
                maxNode = 100
            else:
                maxNode = 100000

            testcase = []

            N = randint(1,maxNode)

            testcase.append(N)
            for i in range(N):
                testcase.append(randint(1,300))

            self.testcases.append(testcase)

test = ProblemTestcase()
test.writeTextFile("bowl.txt",delimeter=":::",seperate=True)