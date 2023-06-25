# Complement

หลังจากที่เราสามารถสร้างเซตได้แล้ว ต่อไปเราจะมาสร้าง Operation หรือ ตัวดำเนินการต่างๆ ที่ใช้สำหรับเซตกัน โดยเราจะเริ่มจาก Complement ก่อน

**Complement** คอมพลีเมนต์ของเซต A คือเซตที่ประกอบด้วยสมาชิกที่เป็นสมาชิกของเอกภพสัมพัทธ์ แต่ไม่เป็นสมาชิกของ A

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นชุดข้อความที่คั่นด้วย Spacebar ทั้งคู่ โดยที่  
**บรรทัดที่ 1** แทนเซตเอกภพสัมพัทธ์ (Relative Universe)  
**บรรทัดที่ 2** แทนเซต A (รับประกันว่าสมาชิกทุกตัวใน A จะอยู่ในเซตเอกภพสัมพัทธ์)  

<u>ข้อมูลส่งออก</u>  
แสดงค่าของ Complement A  

**คำแนะนำ**  
เซตจะยังต้องคงคุณสมบัติเดิมเหมือนกับข้อที่ 1 คือ **มีสมาชิกที่ไม่ซ้ำกัน** และวิธีการแสดงผลที่เหมือนกัน ดังนั้นจึงสามารถนำโค้ดจากข้อที่ 1 มาเขียนเป็น Function ใหม่เ พื่อให้ใช้งานได้ง่ายขึ้น

## Example 1
<pre class="output">
Enter Universe: _0 1 2 3 4 5 6 7 8 9 10_
Enter Set A: _2 3 6 7 9 10_
0 1 4 5 8 
</pre>

## Example 2
<pre class="output">
Enter Universe: _0 1 1 5 2 2 2 2 4 3_
Enter Set A: _4 4 4 4 4_
0 1 5 2 3 
</pre>

## Example 3
<pre class="output">
Enter Universe: _1 2 3 4 5 A B C D E_
Enter Set A: _↵_
1 2 3 4 5 A B C D E 
</pre>

::elab:begincode blank=True
def createSet(label):
    numbers = input(label).split()
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

def printSet(set):
    for item in set:
        print(item, end=" ")

def complement(set,universe):
    result = []
    for n in universe:
        if n not in set:
            result.append(n)
    return result

u = createSet("Enter Universe: ")
a = createSet("Enter Set A: ")

printSet(complement(a,u))
::elab:endcode

::elab:begintest hint="-"
0 1 2 3 4 5 6 7 8 9 10
2 3 6 7 9 10

::elab:endtest

::elab:begintest hint="-"
0 1 1 5 2 2 2 2 4 3
4 4 4 4 4

::elab:endtest

::elab:begintest hint="-"
1 2 3 4 5 A B C D E


::elab:endtest

::elab:begintest hint="-"
123 1215 6454 564 89 489 4564 5646 41 871 9871 817 871 897a 18 w7d187a1 d897 w9 a91 dsd wadaw d awd
::elab:endtest

::elab:begintest hint="-"
::elab:endtest