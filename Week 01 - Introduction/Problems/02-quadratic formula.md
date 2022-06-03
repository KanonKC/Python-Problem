# Quadratic Formula

สมการพหุนามกำลังที่สามารถจัดรูปได้ดังนี้ \(ax^2+bx+c = 0\) เราสามารถหาคำตอบของสมการข้างบนได้โดยใช้สูตรนี้:
\[x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}\]

เขียนโปรแกรมที่รับค่า a,b และ c และคำนวณหาคำตอบ(ค่า x) ของสมการพหุนามกำลังสองนั้นรับประกันว่าข้อมูลที่ทดสอบจะได้ผลลัพธ์ออกมาเป็น 2 คำตอบเสมอ

สามารถหาค่าของรูทสองได้โดยใช้ `sqrt()` จาก Math Library

**ข้อมูลนำเข้า**  
มีทั้งหมด 3 บรรทัด รับค่าเป็น a,b และ c ตามลำดับ โดยแต่ละค่าจะเป็นจำนวนจริง(หมายความว่าจำเป็นจำนวนเต็มหรือทศนิยม และเป็นค่าบวกหรือค่าลบก็ได้)

**ข้อมูลส่งออก**  
แสดงผลลัพธ์ออกมาทั้งหมด 2 คำตอบคือ x1 และ x2 โดยที่ x1 คือค่าที่มาจากการใช้สูตรที่หน้ารูทเป็นบวก และ x2 มาจากการใช้สูตรที่หน้ารูทเป็นลบ ให้ตอบเป็น**ทศนิยม 3 ตำแหน่ง**

## Example 1
<pre class="output">
a: _1_
b: _5_
c: _6_
x1 = -2.000 ,x2 = -3.000
</pre>

## Example 2
<pre class="output">
a: _1_
b: _4_
c: _4_
x1 = -2.000 ,x2 = -2.000
</pre>

## Example 3
<pre class="output">
a: _1_
b: _5.9493_
c: _2.22_
x1 = -0.400 ,x2 = -5.549
</pre>

::elab:begincode blank=True
from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)

print(f"x1 = {x1:.3f} ,x2 = {x2:.3f}")
::elab:endcode

::elab:begintest hint="-"
1
5
6
::elab:endtest

::elab:begintest hint="-"
1
4
4
::elab:endtest

::elab:begintest hint="-"
1
5.9493
2.22
::elab:endtest

::elab:begintest hint="-"
25
100
25
::elab:endtest


::elab:begintest hint="-"
53.21
100.26
2.01
::elab:endtest

::elab:begintest hint="-"
9
25
16
::elab:endtest

::elab:begintest hint="-"
100
1000
100
::elab:endtest