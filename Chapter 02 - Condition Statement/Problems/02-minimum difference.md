# Minimum Difference

เรามีจำนวนนึงให้เป็น x และมีจำนวนอีก 3 ตัวคือ a, b, c เราต้องการเลือกจำนวนใน 3 ตัวนี้มา 1 ตัวที่มีค่าใกล้เคียงกับ x มากที่สุด

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 4 บรรทัด แต่ละบรรทัดจะรับค่าเป็นจำนวนเต็มทั้งหมด  
บรรทัดที่ 1 รับค่า x ที่ใช้เปรียบเทียบกับอีก 3 ค่าข้างล่าง  
บรรทัดที่ 2,3,4 รับค่า a,b,c ตามลำดับ

<u>ข้อมูลส่งออก</u>  
แสดงค่าใน a,b หรือ c ตัวเดียวที่มีค่าใกล้เคียงกับค่า x มากที่สุด

**ข้อแนะนำ**  
สามารถใช้คำสั่ง `abs()` ได้ ซึ่งฟังก์ชันนี้จะคืนค่าสัมบูรณ์(ค่าบวก) ออกมาตลอด เช่น `abs(-4)` ก็จะมีค่าเป็น `4` (ในคณิตศาสตร์ก็คือค่าสัมบูรณ์เหมือนกันกับ `|-4| = 4`)

**อธิบาย:** ให้ x = 1 เพราะฉะนั้นตัวที่ใกล้กับเลข 1 มากที่สุดก็คือ 2

::elab:begincode blank=True
x = int(input())
a = int(input())
b = int(input())
c = int(input())

minimum_value = a
minimum = abs(x-a)

if abs(x-b) < minimum:
    minimum_value = b
    minimum = abs(x-b)
if abs(x-c) < minimum:
    minimum_value = c
    minimum = abs(x-c)

print(f"{minimum_value} is closest to {x}")
::elab:endcode

::elab:begintest hint="-"
1
2
3
4
::elab:endtest

::elab:begintest hint="-"
2
1
2
3
::elab:endtest

::elab:begintest hint="-"
0
-2
-1
10
::elab:endtest

::elab:begintest hint="-"
1
5
-5
10
::elab:endtest

::elab:begintest hint="-"
-125
9952
-1222
1543
::elab:endtest

::elab:begintest hint="-"
1
99999
99998
99997
::elab:endtest

::elab:begintest hint="-"
-1999
125
-699
1050
::elab:endtest