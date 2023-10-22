from generator import TestcaseGenerator
from random import randint,random

class ProblemTestcase(TestcaseGenerator):

    CUSTOM = True

    def customGenerator(self) -> None:
        for t in range(10):

            if t < 4:
                maxNode = 5
            else:
                maxNode = 100

            testcase = []

            N = randint(1,maxNode)
            E = randint(0,(N*(N-1))//2)
            Q = randint(1,maxNode)

            testcase.append(N)
            testcase.append(E)
            testcase.append(Q)

            for i in range(E):
                u = randint(0,N-1)
                v = randint(0,N-1)
                testcase.append(f"{u} {v}")

            for i in range(Q):
                u = randint(0,N-1)
                v = randint(0,N-1)
                testcase.append(f"{u} {v}")

            self.testcases.append(testcase)

test = ProblemTestcase()
test.writeElabsheet()