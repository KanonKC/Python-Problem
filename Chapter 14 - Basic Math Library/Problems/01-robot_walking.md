# Robot Walking

หุ่นยนต์ตัวหนึ่งสามารถเคลื่อนที่ได้ 2 มิติ สามารถเคลื่อนที่ไปในทิศทางต่างๆ ดังนี้  

เดินไปข้างหน้า (U)  
เดินถอยหลัง (D)  
เดินไปซ้าย (L)  
เดินขวา (R)  

เขียนโปรแกรมที่จะรับลำดับการเดินของหุ่นยนต์แล้วคำนวณว่าหลังจากที่เดินเรียบร้อยแล้วหุ่นยนต์จะอยู่ห่างจากจุดเริ่มต้นเท่าไร

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเข้ามาเป็นสายอักขระ แทนลำดับการเดินของหุ่นยนต์ ประกอบด้วย U, D, L และ R เท่านั้น

<u>ข้อมูลส่งออก</u>  
แสดงทศนิยม 2 ตำแหน่ง แทนระยะทางที่หุ่นยนต์อยู่ห่างจากจุดเริ่มต้น

## Example 1
<pre class="output">
Enter walking sequences: _RRRUUUU_
Distance: 5.00
</pre>

## Example 2
<pre class="output">
Enter walking sequences: _RDRDULUL_
Distance: 0.00
</pre>

## Example 3
<pre class="output">
Enter walking sequences: _LLLLL_
Distance: 5.00
</pre>

::elab:begincode blank=True
from math import sqrt

walkingSequences = input("Enter walking sequences: ")

x,y = 0,0

for i in walkingSequences:
    if i == "L":
        x -= 1
    elif i == "R":
        x += 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1

distance = sqrt(x**2 + y**2)
print(f"Distance: {distance:.2f}")
::elab:endcode

::elab:begintest hint="-"
RRRUUUU

::elab:endtest

::elab:begintest hint="-"
RDRDULUL

::elab:endtest

::elab:begintest hint="-"
LLLLL

::elab:endtest

::elab:begintest hint="-"
URLDURLUDLURLUDLRUUDLRULULD

::elab:endtest

::elab:begintest hint="-"
DLURLUDURLUDLURLUDLURLDRULDURULDLRULR

::elab:endtest

::elab:begintest hint="-"


::elab:endtest