# Math Operation

เขียนโปรแกรมที่รับตัวเลข 2 ตัว จากนั้นคำนวณหาผลลัพธ์จากการนำมา บวก ลบ คูณ หาร (สำหรับการหาร ให้เลขตัวแรกเป็นตัวตั้ง และตัวที่สองเป็นตัวหาร)

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นเลขจำนวนเต็มทั้งคู่

<u>ข้อมูลส่งออก</u>  
มีทั้งหมด 4 บรรทัด โดย  
**บรรทัดที่ 1** แสดงผลบวกของ 2 จำนวน  
**บรรทัดที่ 2** แสดงผลลบของ 2 จำนวน  
**บรรทัดที่ 3** แสดงผลคูณของ 2 จำนวน  
**บรรทัดที่ 4** แสดงผลหารของ 2 จำนวน โดยแสดงให้อย่ในรูป*ทศนิยม 2 ตำแหน่ง*  

## Example 1
<pre class="output">
_10_
_5_
a + b = 15  
a - b = 5   
a * b = 50  
a / b = 2.00
</pre>

## Example 2
<pre class="output">
_5_
_2_
a + b = 7
a - b = 3
a * b = 10
a / b = 2.50
</pre>

**Hint:** สำหรับการแสดงผลในรูปแบบข้างบน จะให้ไอเดียการเขียนจากโค้ดข้างล่างนี้เลย

<pre class="output">
x = 12.6485453112
print(f"x = {x1}")
print(f"x (rounded) = {x1:.3f}")
</pre>

::elab:begincode blank=True
a = int(input())
b = int(input())

print(f"a + b = {a+b}")
print(f"a - b = {a-b}")
print(f"a * b = {a*b}")
print(f"a / b = {a/b:.2f}")
::elab:endcode

::elab:begintest hint="-"
10
5
::elab:endtest
::elab:begintest hint="-"
5
2
::elab:endtest
::elab:begintest hint="-"
629977
289913
::elab:endtest
::elab:begintest hint="-"
356219
-975204
::elab:endtest
::elab:begintest hint="-"
921527
-326427
::elab:endtest
::elab:begintest hint="-"
-203551
872018
::elab:endtest
::elab:begintest hint="-"
711112
726350
::elab:endtest
::elab:begintest hint="-"
508983
-883609
::elab:endtest
::elab:begintest hint="-"
-576612
-44399
::elab:endtest
::elab:begintest hint="-"
-183492
-619464
::elab:endtest