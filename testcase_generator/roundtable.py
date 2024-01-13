from generator import TestcaseGenerator
from random import randint,random,shuffle

class ProblemTestcase(TestcaseGenerator):

    CUSTOM = True

    def customGenerator(self) -> None:
        for t in range(8):

            if t < 3:
                maxNode = 100
            else:
                maxNode = 200000

            testcase = []

            N = randint(1,maxNode)

            testcase.append(N)
            line2 = [str(i+1) for i in range(N)]
            shuffle(line2)
            testcase.append(" ".join(line2))
            
            self.testcases.append(testcase)

test = ProblemTestcase()
test.writeTextFile("roundtable.txt",delimeter=":::")