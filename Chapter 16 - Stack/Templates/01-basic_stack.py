STACK = []

def push(value):
    # Implement this method
    pass

def pop():
    # Implement this method
    pass

def top():
    # Implement this method
    pass

def empty():
    # Implement this method
    pass

def show():
    # Implement this method
    pass

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