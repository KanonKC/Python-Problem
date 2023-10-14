STACK = []
pointer = -1
size = 0

def push(value):
    global pointer,size
    if pointer + 1 == size:
        size += 1
        STACK.append(value)
    else:
        STACK[pointer + 1] = value
    pointer += 1

def empty():
    global pointer
    return pointer == -1

def pop(remove=True):
    global pointer
    if pointer == -1:
        return None

    rtn = STACK[pointer]
    if remove:
        pointer -= 1
    return rtn

def show():
    global pointer
    print(STACK[:pointer+1])

operators = ["-","+","/","*"]
result = []

expression = input("Enter expression: ").split()

for char in expression:
    if char not in operators:
        result.append(char)
    else:
        while not empty():
            if operators.index(pop(False)) >= operators.index(char):
                result.append(pop())
            else:
                break
        push(char)

while not empty():
    result.append(pop())

print(" ".join(result))

