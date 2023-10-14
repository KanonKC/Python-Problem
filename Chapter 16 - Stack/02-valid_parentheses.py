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

text = input("Enter parentheses: ")

openParen = ["(","[","{"]
closeParen = [")","]","}"]
pairParen = {
    ")":"(",
    "]":"[",
    "}":"{"
}

for paren in text:
    if paren in openParen:
        push(paren)
    elif paren in closeParen:
        if pop(False) != pairParen[paren]:
            print("Invalid")
            break
        else:
            pop()
else:
    if empty():
        print("Valid")
    else:
        print("Invalid")