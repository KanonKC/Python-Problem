# Right Triangle

*(โจทย์ข้อนี้นำมาจากหนังสืิอ Python ๑๐๑ ภาควิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย)*  

ในโจทย์ข้อนี้จะสนใจสามเหลี่ยมมุมฉากที่ยาวทุกด้านเป็น**จำนวนเต็ม**  

เขียนโปรแกรมที่รับค่าเส้นรอบรูป และหาจำนวนเต็มที่มากที่สุดที่เป็นความยาวของด้านตรงข้ามมุมฉากของสามเหลี่ยมมุมฉาก เช่น ให้สามเหลี่ยมมุมฉากที่มีเส้นรอบรูป 90 หน่วยจะมีสามเหลี่ยมมุมฉากตามข้อกำหนด 2 รูปคือ 15,36,39 และ 9,40,41 คำตอบก็คือ 41 เพราะเป็นด้านตรงข้ามมุมฉากที่ยาวที่สุด

สามารถใช้ `Math Library` ในการแก้ปัญหาข้อนี้ได้

**ข้อมูลนำเข้า**  
มีบรรทัดเดียว เป็นจำนวนเต็มบวก แทนความยาวเส้นรอบรูป

**ข้อมูลส่งออก**  
มีบรรทัดเดียว แสดงความยาวของด้านตรงข้ามมุมฉากที่ยาวที่สุดตามข้อกำหนด

## Example 1
<pre class="output">
_30_
13
</pre>

## Example 2
<pre class="output">
_90_
41
</pre>

::elab:begincode blank=True
from math import sqrt

n = int(input())
max_length = 0
for a in range(1,n):
    for b in range(1,n):
        res = sqrt(a**2 + b**2)
        if a+b+res == n and int(res) == res and res > max_length:
            max_length = int(res)

print(max_length)
::elab:endcode

::elab:begintest hint="-"
30
::elab:endtest
::elab:begintest hint="-"
90
::elab:endtest
::elab:begintest hint="-"
12
::elab:endtest
::elab:begintest hint="-"
24
::elab:endtest
::elab:begintest hint="-"
30
::elab:endtest
::elab:begintest hint="-"
70
::elab:endtest
::elab:begintest hint="-"
72
::elab:endtest
::elab:begintest hint="-"
120
::elab:endtest
::elab:begintest hint="-"
154
::elab:endtest
::elab:begintest hint="-"
182
::elab:endtest
::elab:begintest hint="-"
210
::elab:endtest
::elab:begintest hint="-"
252
::elab:endtest