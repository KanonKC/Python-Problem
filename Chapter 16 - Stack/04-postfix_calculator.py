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
result = 0

expression = input("Enter postfix expression: ").split()

for char in expression:
    if char not in operators:
        push(int(char))
    else:
        op1 = pop()
        op2 = pop()
        result = 0

        if char == "-":
            result = op2 - op1
        elif char == "+":
            result = op2 + op1
        elif char == "/":
            result = op2 / op1
        elif char == "*":
            result = op2 * op1
        push(result)

print(f"= {result:.2f}")