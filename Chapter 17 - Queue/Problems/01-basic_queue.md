# Basic Queue

ใช้ภาษา Python ในการสร้าง Queue โดยจะมีฟังก์ชันการทำงานพื้นฐาน ดังนี้
- `enqueue(value)` ใส่ข้อมูล `value` ลงไปใน Queue ไม่ทำการคืนค่าใด ๆ ออกมา
- `dequeue()` นำข้อมูลตัวแรกสุดของ Queue ออกมา และคืนค่าข้อมูลนั้นออกมาด้วย หากไม่มีข้อมูลอยู่ใน Queue ให้คืนค่า `None` ออกมา
- `head()` คืนค่าข้อมูลตัวแรกสุดของ Queue ออกมา หากไม่มีข้อมูลอยู่ใน Queue  ให้คืนค่า `None` ออกมา(ทำงานเหมือน `pop()` แต่ไม่ได้นำข้อมูลออกมาด้วย)
- `empty()` ตรวจสอบดูว่า Queue ว่างหรือไม่ ถ้าว่างให้คืนค่า `True` ถ้าไม่ว่างให้คืนค่า `False` ออกมา
- `show()` แสดงค่าของข้อมูลใน Queue ทั้งหมด ไม่ต้องคืนค่าอะไรออกมา

สามารถนำโค้ดเริ่มต้นได้จากตรงนี้
```python
QUEUE = []
first = -1
last = -1

def enqueue(value):
    # Implement this method
    pass

def dequeue():
    # Implement this method
    pass

def head():
    # Implement this method
    pass

def empty():
    # Implement this method
    pass

def show():
    # Implement this method
    pass

while True:
    command = input("Select method (enqueue/dequeue/first/empty/show): ").split()

    if len(command) == 0:
        break
    elif command[0] == "enqueue":
        enqueue(command[1])
        print(f"Enqueue -> {command[1]}")
    elif command[0] == "dequeue":
        print(f"Dequeue -> {dequeue()}")
    elif command[0] == "first":
        print(f"First -> {first()}")
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "show":
        show()

```

## Example 1
<pre class="output">
Select method (enqueue/dequeue/head/empty/show): _enqueue A_
Enqueue -> A
Select method (enqueue/dequeue/head/empty/show): _enqueue B_
Enqueue -> B
Select method (enqueue/dequeue/head/empty/show): _enqueue C_
Enqueue -> C
Select method (enqueue/dequeue/head/empty/show): _show_
['A', 'B', 'C']
Select method (enqueue/dequeue/head/empty/show): _head_
head -> A
Select method (enqueue/dequeue/head/empty/show): _dequeue_
Dequeue -> A
Select method (enqueue/dequeue/head/empty/show): _dequeue_
Dequeue -> B
Select method (enqueue/dequeue/head/empty/show): _empty_
False
Select method (enqueue/dequeue/head/empty/show): _enqueue D_
Enqueue -> D
Select method (enqueue/dequeue/head/empty/show): _enqueue E_
Enqueue -> E
Select method (enqueue/dequeue/head/empty/show): _dequeue_
Dequeue -> C
Select method (enqueue/dequeue/head/empty/show): _dequeue_
Dequeue -> D
Select method (enqueue/dequeue/head/empty/show): _dequeue_
Dequeue -> E
Select method (enqueue/dequeue/head/empty/show): _dequeue_
Dequeue -> None
Select method (enqueue/dequeue/head/empty/show): _show_
[]
Select method (enqueue/dequeue/head/empty/show): _empty_
True
Select method (enqueue/dequeue/head/empty/show): _↵_

</pre>

::elab:begincode blank=True
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
::elab:endcode

::elab:begintest hint="-"
enqueue A
enqueue B
enqueue C
show
head
dequeue
dequeue
empty
enqueue D
enqueue E
dequeue
dequeue
dequeue
dequeue
show
empty


::elab:endtest

::elab:begintest hint="-"
show
head
dequeue
show
dequeue
enqueue 1
enqueue 2
dequeue
dequeue


::elab:endtest

::elab:begintest hint="-"
enqueue A
enqueue B
enqueue C
dequeue
dequeue
dequeue
dequeue
dequeue
show
empty
enqueue D
enqueue E
show
empty


::elab:endtest