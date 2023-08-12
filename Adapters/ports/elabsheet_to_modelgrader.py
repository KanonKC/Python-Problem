def convert(text):
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