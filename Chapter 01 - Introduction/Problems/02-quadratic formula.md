# Quadratic Formula

สมการพหุนามกำลังที่สามารถจัดรูปได้ดังนี้ \(ax^2+bx+c = 0\) เราสามารถหาคำตอบของสมการข้างบนได้โดยใช้สูตรนี้:
\[x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}\]

เขียนโปรแกรมที่รับค่า a,b และ c และคำนวณหาคำตอบ(ค่า x) ของสมการพหุนามกำลังสองนั้นรับประกันว่าข้อมูลที่ทดสอบจะได้ผลลัพธ์ออกมาเป็น 2 คำตอบเสมอ

สามารถหาค่าของรูทสองได้โดยใช้ `sqrt()` จาก Math Library

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 3 บรรทัด รับค่าเป็น a,b และ c ตามลำดับ โดยแต่ละค่าจะเป็นจำนวนจริง(หมายความว่าจำเป็นจำนวนเต็มหรือทศนิยม และเป็นค่าบวกหรือค่าลบก็ได้)

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ออกมาทั้งหมด 2 คำตอบคือ x1 และ x2 โดยที่ x1 คือค่าที่มาจากการใช้สูตรที่หน้ารูทเป็นบวก และ x2 มาจากการใช้สูตรที่หน้ารูทเป็นลบ ให้ตอบเป็น**ทศนิยม 3 ตำแหน่ง**

::elab:begincode blank=True
from math import sqrt

a = float(input())
b = float(input())
c = float(input())

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