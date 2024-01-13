from random import random,randint

class StandardTestcaseInteger:
    def __init__(self,min=0,max=100):
        self.min = min
        self.max = max

class StandardTestcaseFloat:
    def __init__(self,min=0,max=100):
        self.min = min
        self.max = max

class StandardTestcaseString:
    def __init__(self,sampleSpaces=[]):
        self.sampleSpaces = sampleSpaces

class StandardTestcaseBoolean:
    def __init__(self,boolean):
        self.boolean = boolean

class TestcaseGenerator:

    CUSTOM = False
    COUNT = 0
    INPUT_TYPE = []

    def __init__(self):
        self.testcases = []

    def standardGenerator(self):
        count = self.COUNT
        input_type = self.INPUT_TYPE
        for _ in range(count):
            testcase = []

            for j in range(len(input_type)):
                if isinstance(input_type[j],StandardTestcaseString):
                    testcase.append(input_type[j].sampleSpaces[randint(0,len(input_type[j].sampleSpaces)-1)])

                elif isinstance(input_type[j],StandardTestcaseInteger):
                    testcase.append(randint(input_type[j].min,input_type[j].max))

                elif isinstance(input_type[j],StandardTestcaseFloat):
                    testcase.append(round(randint(input_type[j].min,input_type[j].max) + random(),3))

            self.testcases.append(testcase)

    def customGenerator(self) -> None:
        """
        Store testcases to self.testcases
        Return None
        """
        pass

    def writeTextFile(self,filename="testcase.txt",show=False,delimeter="----------",seperate=False) -> None:
        """
        Write testcases to text file
        Return None
        """
        if self.CUSTOM:
            self.customGenerator()
        else:
            self.standardGenerator()
        if seperate:
            for i in range(len(self.testcases)):
                with open(f"{filename}{i+1}","w") as file:
                    text = ""
                    text += "\n".join([str(j) for j in self.testcases[i]])
                    text += f"\n{delimeter}\n"
                    file.write(text)
                    print("Testcases saved to",f"{filename}{i+1}")
                    if show:
                        print(text)
        else:
            with open(filename,"w") as file:
                text = ""
                for testcase in self.testcases:
                    text += "\n".join([str(j) for j in testcase])
                    text += f"\n{delimeter}\n"
                file.write(text)
                print("Testcases saved to",filename)
                if show:
                    print(text)

    def writeElabsheet(self,filename="testcase.txt",show=False) -> None:
        """
        Write testcases in Elabsheet format to text file
        Return None
        """
        if self.CUSTOM:
            self.customGenerator()
        else:
            self.standardGenerator()
        with open(filename,"w") as file:
            text = ""
            for testcase in self.testcases:
                text += '::elab:begintest hint="-"\n'
                text += "\n".join([str(j) for j in testcase]) + "\n"
                text += '::elab:endtest\n'
                
            file.write(text)
            print("Testcases saved to",filename)
            if show:
                print(text)

# Export this class to be used in other files
__all__ = ["TestcaseGenerator"]