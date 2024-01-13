from generator import TestcaseGenerator
from random import randint,random

class ProblemTestcase(TestcaseGenerator):

    CUSTOM = True

    def customGenerator(self) -> None:
        for t in range(9):

            if t < 4:
                maxNode = 300
            else:
                maxNode = 200000

            n = randint(1,maxNode)
            k = randint(1,n-1)
            t = randint(1,n)

            self.testcases.append([f"{n} {k} {t}"])

test = ProblemTestcase()
test.writeTextFile("thief.txt",delimeter=":::",show=True)