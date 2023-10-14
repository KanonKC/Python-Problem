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

def show():
    global first,last
    print(QUEUE[first:last+1])

while True:
    command = input("Select method [(e)nqueue/(d)equeue]: ").split()

    if len(command) == 0:
        break
    elif command[0] == "e":
        enqueue(command[1])
    elif command[0] == "d":
        dequeue()
    

    show()
