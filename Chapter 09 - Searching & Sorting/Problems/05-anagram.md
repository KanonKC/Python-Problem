# Anagram

**คำสลับอักษร (Anagram)** คือข้อความเกิดจากการนำตัวอักษรในอีกข้อความหนึ่งมาเรียงสลับที่กัน เช่น Eleven plus two เป็นอะนาแกรมของ Twelve plus one หรือ A Decimal Point เป็นอะนาแกรมของ I'm a Dot in Place  

ในโจทย์ข้อนี้ เราจะรับข้อความเข้ามา 2 ชุด จากนั้นลองตรวจสอบว่า 2 ข้อความนั้นเป็นอะนาแกรมกันหรือไม่

<u>ข้อมูลนำเข้า</u>  
**มี 2 บรรทัด** รับเป็นข้อความทั้งคู่

<u>ข้อมูลส่งออก</u>  
แสดงข้อความเพื่อบอกว่า 2 ข้อความนั้นเป็นอะนาแกรมกันหรือไม่

## Example 1
<pre class="output">
Enter text 1: _Listen_
Enter text 2: _Silent_
Anagram!
</pre>

## Example 2
<pre class="output">
Enter text 1: _melon_
Enter text 2: _grape_
Not anagram!
</pre>

## Example 3
<pre class="output">
Enter text 1: _school master_
Enter text 2: _the classroom_
Anagram!
</pre>

::elab:begincode blank=True
text1 = input("Enter text 1: ").lower()
text2 = input("Enter text 2: ").lower()

if sorted(text1) == sorted(text2):
    print("Anagram!")
else:
    print("Not anagram!")
::elab:endcode

::elab:begintest hint="-"
Listen
Silent
::elab:endtest

::elab:begintest hint="-"
melon
grape
::elab:endtest

::elab:begintest hint="-"
school master
the classroom
::elab:endtest

::elab:begintest hint="-"
debit?
bited
::elab:endtest

::elab:begintest hint="-"
Cinema
Iceman
::elab:endtest

::elab:begintest hint="-"
asdw5ads1dw
yu51l4iu12i
::elab:endtest