from generator import TestcaseGenerator
from random import randint,random,shuffle

class ProblemTestcase(TestcaseGenerator):

    CUSTOM = True

    def customGenerator(self) -> None:
        for t in range(9):

            if t < 4:
                maxNode = 100
            else:
                maxNode = 10000


            N = randint(1,maxNode)

            line2 = [i+1 for i in range(N)]
            shuffle(line2)

            self.testcases.append([N,*line2])

test = ProblemTestcase()
test.writeTextFile("hand_change.txt",delimeter=":::")
