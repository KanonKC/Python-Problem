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

def pop():
    global pointer
    if pointer == -1:
        return None

    rtn = STACK[pointer]
    pointer -= 1
    return rtn

def top():
    global pointer
    if pointer == -1:
        return None

    rtn = STACK[pointer]
    return rtn

def empty():
    global pointer
    return pointer == -1

def show():
    global pointer
    print(STACK[:pointer+1])

while True:
    command = input("Select method (push/pop/top/empty/show): ").split()

    if len(command) == 0:
        break
    elif command[0] == "push":
        push(command[1])
        print(f"Push -> {command[1]}")
    elif command[0] == "pop":
        print(f"Pop -> {pop()}")
    elif command[0] == "top":
        print(f"Top -> {top()}")
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "show":
        show()