QUEUE = []
first = -1
last = -1

def enqueue(value):
    global first,last
    QUEUE.append(value)

    if first == -1 and last == -1:
        first = 0
        last = 0
    else:
        last += 1

def dequeue():
    global first,last
    if first > last or first == -1:
        return None

    rtn = QUEUE[first]
    first += 1
    return rtn

def head():
    global first,last
    if first > last or first == -1:
        return None

    rtn = QUEUE[first]
    return rtn

def empty():
    global first,last
    return (first == -1 and last == -1) or first > last

def show():
    global first,last
    print(QUEUE[first:last+1])

while True:
    command = input("Select method (enqueue/dequeue/head/empty/show): ").split()

    if len(command) == 0:
        break
    elif command[0] == "enqueue":
        enqueue(command[1])
        print(f"Enqueue -> {command[1]}")
    elif command[0] == "dequeue":
        print(f"Dequeue -> {dequeue()}")
    elif command[0] == "head":
        print(f"head -> {head()}")
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "show":
        show()
