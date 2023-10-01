import os
import requests


def getDir():
    for dir in os.listdir('./'):
        if f"Chapter 0{chapter}" in dir:
            return dir
        if f"Chapter {chapter}" in dir:
            return dir 


def parser(text):
    title = text.split('\n')[0].split('#')[1].strip()
    
    betweenCode = text.split('::elab:begincode blank=True')

    description = betweenCode[0]
    
    for i in range(len(description)):
        if description[i] == '\n':
            j = i
            while description[j] == '\n' or  description[j] == '\r':
                j += 1
            description = description[j:]
            break

    betweenTest = betweenCode[1].split('::elab:endcode')
    
    code = betweenTest[0]

    testcases = betweenTest[1].split('::elab:begintest hint="-"')
    testcaseList = [i.split('::elab:endtest')[0] for i in testcases if i.strip() != '']

    finalTestcaseList = []

    for test in testcaseList:
        if test[0] == '\n':
            finalTestcaseList.append(test[1:])
        else:
            finalTestcaseList.append(test)

    inputData = {
        "title": title,
        "language": "py",
        "description": description,
        "solution": code,
        "testcases": finalTestcaseList,
        "time_limit": 1.5
    }

    return inputData

def displayParser(parsed):
    print("title",parsed["title"])
    print("description",parsed["description"])
    print("solution",parsed["solution"])
    print("testcases")
    for i in parsed["testcases"]:
        print(i)
        print(":::")
    print("time_limit",parsed["time_limit"])

chapter = int(input("Chapter: "))
file_set = [int(i) for i in input("File No: ").split()]

for file_no in file_set:
    directory = f"./{getDir()}"

    try:
        file = os.listdir(f"{directory}/Problems")[file_no-1]
        print(f"Uploading {file} Response...",end="")

        f = open(f"{directory}/Problems/{file}",'r',encoding='utf8')
        # f = open(f"{directory}/Problems/02-quadratic formula.md",'r',encoding='utf8')
        data = f.read()
        body = parser(data)

        displayParser(body)

        response = requests.post('http://localhost:8004/api/accounts/4/problems',json=body)
        print(f"{response}")
    except Exception as err:
        print(f"<Error []>\n{err}")

print("Done")

# ISSUE

# <Response [406]> 07-reminder_theorem.md
# <Response [406]> 08-duo_eater.md

# <Response [406]> 09-qualification.md
# <Response [406]> 10-buzzloteli.md
# <Response [406]> 11-simple_calculator.md

# 12-...
# <Error []> 13-basic_forloop.md

# <Response [406]> 04-parallel.md

# <Error []> 05-list_generation.md
