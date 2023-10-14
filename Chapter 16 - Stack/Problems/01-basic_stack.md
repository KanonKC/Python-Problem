# Basic Stack

ใช้ภาษา Python ในการสร้าง Stack โดยจะมีฟังก์ชันการทำงานพื้นฐาน ดังนี้
- `push(value)` ใส่ข้อมูล `value` ลงไปใน Stack ไม่ทำการคืนค่าใด ๆ ออกมา
- `pop()` นำข้อมูลล่าสุดของ Stack ออกมา และคืนค่าข้อมูลนั้นออกมาด้วย หากไม่มีข้อมูลอยู่ใน Stack ให้คืนค่า `None` ออกมา
- `top()` คืนค่าข้อมูลล่าสุดของ Stack ออกมา หากไม่มีข้อมูลอยู่ใน Stack  ให้คืนค่า `None` ออกมา(ทำงานเหมือน `pop()` แต่ไม่ได้นำข้อมูลออกมาด้วย)
- `empty()` ตรวจสอบดูว่า Stack ว่างหรือไม่ ถ้าว่างให้คืนค่า `True` ถ้าไม่ว่างให้คืนค่า `False` ออกมา
- `show()` แสดงค่าของข้อมูลใน Stack ทั้งหมด ไม่ต้องคืนค่าอะไรออกมา

สามารถนำโค้ดเริ่มต้นได้จากตรงนี้
```python
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
```

## Example 1
<pre class="output">
Select method (push/pop/top/empty/show): _push A_
Push -> A
Select method (push/pop/top/empty/show): _push B_
Push -> B
Select method (push/pop/top/empty/show): _push C_
Push -> C
Select method (push/pop/top/empty/show): _show_
['A', 'B', 'C']
Select method (push/pop/top/empty/show): _empty_
False
Select method (push/pop/top/empty/show): _top_
Top -> C
Select method (push/pop/top/empty/show): _show_
['A', 'B', 'C']
Select method (push/pop/top/empty/show): _pop_
Pop -> C
Select method (push/pop/top/empty/show): _show_
['A', 'B']
Select method (push/pop/top/empty/show): _pop_
Pop -> B
Select method (push/pop/top/empty/show): _pop_
Pop -> A
Select method (push/pop/top/empty/show): _pop_
Pop -> None
Select method (push/pop/top/empty/show): _show_
[]
Select method (push/pop/top/empty/show): _empty_
True
Select method (push/pop/top/empty/show): __↵__

</pre>

::elab:begincode blank=True
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
::elab:endcode

::elab:begintest hint="-"
push A
push B
push C
show
empty
top
show
pop
show
pop
pop
pop
show
empty


::elab:endtest

::elab:begintest hint="-"
pop
top
show
push A
pop
empty
push B
show
empty
push C
show
empty


::elab:endtest

::elab:begintest hint="-"
push A
push B
push C
pop
pop
push D
push E
show


::elab:endtest