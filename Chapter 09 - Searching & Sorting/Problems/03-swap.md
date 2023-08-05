# Swap

ในโจทย์ข้อนี้เราจะลองสลับค่าของข้อมูลใน List กัน  

ใข้ฟังก์ชันนี้ในการแสดงผล List:
```python
def printList(list):
    for i in list:
        print(i, end=' ')
    print()
```

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1** รับเป็นข้อความที่จะสร้างเป็น List โดยสมาชิกแต่ละตัวจะคั่นด้วย Spacebar  
**ตั้งแต่บรรทัดที่ 2** รับเป็นข้อความตัวเลข 2 ตัวคั่นด้วย Spacebar โดยจะแทน Index ของ List ที่ต้องการสลับค่า จะหยุดเมื่อรับค่าเข้ามาเป็น `-1 -1`

<u>ข้อมูลส่งออก</u>  
มีการแสดงค่าทุกครั้งที่มีการสลับเกิดขึ้น โดยมีลักษณะตามฟังก์ชัน `printList()` 

## Example 1
<pre class="output">
Enter a list: _A B C D E_
Swap index: _1 3_
A D C B E 
Swap index: _0 1_
D A C B E 
Swap index: _3 2_
D A B C E 
Swap index: _-1 -1_
</pre>

::elab:begincode blank=True
def printList(list):
    for i in list:
        print(i, end=' ')
    print()

container = [i for i in input("Enter a list: ").split()]

while True:
    x,y = [int(i) for i in input("Swap index: ").split()]
    if x == -1 and y == -1:
        break
    
    tmp = container[x]
    container[x] = container[y]
    container[y] = tmp

    printList(container)
::elab:endcode

::elab:begintest hint="-"
A B C D E
1 3
0 1
3 2
-1 -1
::elab:endtest

::elab:begintest hint="-"
10
-1 -1
::elab:endtest

::elab:begintest hint="-"
4 8 2 7 5 1
3 5
0 1
2 4
-1 -1
::elab:endtest