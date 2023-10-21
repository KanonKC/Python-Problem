from testcase_generator.generator import TestcaseGenerator
from random import randint,random

class ProblemTestcase(TestcaseGenerator):
    
    def generate(self) -> None:
        for _ in range(10):
            testcase = []

            N = randint(0,100)
            E = randint(0,100)
            Q = randint(0,100)

            testcase.append(N)
            testcase.append(E)
            testcase.append(Q)

            for i in range(E):
                u = randint(0,N-1)
                v = randint(0,N-1)
                self.testcases.append(f"{u} {v}")

            for i in range(Q):
                node = randint(0,N-1)
                testcase.append(node)

            self.testcases.append(testcase)


if __name__ == "__main__":
    test = ProblemTestcase()
    test.generate()
    # test.writeTextFile()