# Decimal To Binary

**Decimal** คือเลขฐาน 10 คือระบบตัวเลขที่เราใช้ในชีวิตประจำวัน โดยที่มีตัวเลขทั้งหมด 10 ตัวก็คือ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 เมื่อนับถึง 9 แล้วจะต้องขึ้นหลักถัดไปเช่น  
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, <span style="color: red;">10,</span> 11, 12, 13, ... , 97, 98, 99, <span style="color: red;">100</span>  

**Binary** คือเลขฐาน 2 คือระบบตัวเลขโดยที่มีตัวเลขทั้งหมด 2 ตัวก็คือ 0,1 เท่านั้น เมื่อนับถึง 1 แล้วจะต้องขึ้นหลักถัดไปเช่น  
0, 1, <span style="color: red;">10,</span> 11,<span style="color: red;"> 100,</span> 101, 110, 111, <span style="color: red;">1000</span>  

จะเห็นว่าการนับเลขฐาน 2 จะนับได้เร็วกว่าเลขฐาน 10 เพราะจำนวนในการใช้นับมีน้อยกว่ามาก  
โดยเราสามารถแปลงจากเลขฐาน 10 ไปเป็นเลขฐาน 2 ได้โดยทำตามรูปด้านล่าง

<img src="https://cdn1.byjus.com/wp-content/uploads/2021/09/Decimal-to-binary.png">

ให้เขียนโปรแกรมโดยรับเลขฐาน 10 เข้ามาและแปลงไปเป็นเลขฐาน 2

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว โดยรับค่าเป็นจำนวนเต็มเลขฐานสิบ n เมื่อ n ≥ 0

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์เป็นเลขฐานสองที่ได้จากการแปลง

## Example 1
<pre class="output">
_0_
0
</pre>

## Example 2
<pre class="output">
_3_
11
</pre>

## Example 3
<pre class="output">
_8_
1000
</pre>

## Example 4
<pre class="output">
_15_
1111
</pre>

::elab:begincode blank=True
n = int(input())
binary = ""

if n == 0:
    binary = "0"
while n != 0:
    binary = f"{n%2}{binary}"
    n //= 2
    
print(binary)
::elab:endcode

::elab:begintest hint="-"
0
::elab:endtest
::elab:begintest hint="-"
2
::elab:endtest
::elab:begintest hint="-"
5
::elab:endtest
::elab:begintest hint="-"
7
::elab:endtest
::elab:begintest hint="-"
10
::elab:endtest
::elab:begintest hint="-"
55441
::elab:endtest
::elab:begintest hint="-"
26353
::elab:endtest
::elab:begintest hint="-"
12348
::elab:endtest
::elab:begintest hint="-"
52770
::elab:endtest
::elab:begintest hint="-"
87554
::elab:endtest