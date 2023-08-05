# Sorting

การจัดเรียงข้อมูล (Sorting) ถือเป็นเครื่องมือสำคัญอย่างนึงในการเขียนโปรแกรมมาก ดังนั้นในโจทย์ข้อนี้เราจะมาลองเรียงข้อมูลกัน  

รับ List จำนวนเต็มเข้ามา จากนั้นเรียงข้อมูลจากมากไปน้อย  

ใข้ฟังก์ชันนี้ในการแสดงผล List:
```python
def printList(list):
    for i in list:
        print(i, end=' ')
    print()
```

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็นข้อความที่เป็นจำนวนเต็มคั่นด้วย Spacebar

<u>ข้อมูลส่งออก</u>  
แสดงค่าข้อมูลจากมากไปน้อย

## Example 1
<pre class="output">
Enter a list: _5 2 3 1 4_
5 4 3 2 1
</pre>

::elab:begincode blank=True
def printList(list):
    for i in list:
        print(i, end=' ')
    print()

container = [int(i) for i in input("Enter a list: ").split()]

container.sort(reverse=True)

printList(container)
::elab:endcode

::elab:begintest hint="-"
5 2 3 1 4
::elab:endtest

::elab:begintest hint="-"
52 6 9884 21 84654 21 58 8 212 2 2 2 2 0 1212 1 8 45 5 6 3 21
::elab:endtest

::elab:begintest hint="-"
-1 -95 54 -51 -54 654 -654 -56545 -954 212 -654 5 -68 4954 -654
::elab:endtest

::elab:begintest hint="-"
5 4 3 2 1
::elab:endtest

::elab:begintest hint="-"
1
::elab:endtest
