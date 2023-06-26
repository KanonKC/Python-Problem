# Set

**เซต** คือ กลุ่มของสิ่งต่างๆ (Element) ที่เราสนใจ โดยเมื่อกล่าวถึงกลุ่มใดจะสามารถบอกได้แน่นอน ว่าสิ่งใดอยู่กลุ่ม สิ่งใดไม่อยู่ในกลุ่ม  

ในโจทย์ข้อนี้เราจะจำลองการสร้าง Set โดยใช้ `List` ของ Python โดยที่คุณสมบัติของเซตอย่างนึงก็คือ **สมาชิกแต่ละตัวจะต้องไม่ซ้ำกัน**

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็นข้อความหลายตัว โดยแต่ละตัวจะคั่นด้วย Spacebar (Set ที่เราจะออกแบบนี้ ไม่จำเป็นต้องใส่ตัวเลขอย่างเดียว ใส่เป็นคำไปด้วยก็ได้)

<u>ข้อมูลส่งออก</u>  
แสดงสมาชิกทุกตัวในเซตที่เราออกแบบ โดยที่สมาชิกจะต้องมีไม่ซ้ำกัน

## Example 1
<pre class="output">
Enter set: _1 2 3 4 5_
1 2 3 4 5 
</pre>

## Example 2
<pre class="output">
Enter set: _1 5 4 4 1 1 2 3_
1 5 4 2 3 
</pre>

## Example 3
<pre class="output">
Enter set: _ant dog bob cat dog cat_
ant dog bob cat 
</pre>

::elab:begincode blank=True
numbers = input("Enter set: ").split()
result = []

for n in numbers:
    if n not in result:
        result.append(n)

for item in result:
    print(item, end=" ")
::elab:endcode

::elab:begintest hint="-"
1 2 3 4 5

::elab:endtest

::elab:begintest hint="-"
1 5 4 4 1 1 2 3

::elab:endtest

::elab:begintest hint="-"
ant dog bob cat dog cat

::elab:endtest

::elab:begintest hint="-"


::elab:endtest

::elab:begintest hint="-"
A B 1 2 C D 5 6 A C 4 5 1 V A 5 3 A A SD ALSKDL OWIDOW ASLDLWK 123 4 56

::elab:endtest