# Max of Three

เขียนโปรแกรมที่หาค่าที่มากที่สุดของจำนวนทั้ง 3 ตัวนี้

<u>ข้อมูลนำเข้า</u>  
มี 3 บรรทัด เป็นจำนวนเต็มแทนทั้งคู่

<u>ข้อมูลส่งออก</u>  
จำนวนที่มีค่ามากที่สุด

::elab:begincode blank=True
a = int(input())
b = int(input())
c = int(input())

maximum_value = a

if b > maximum_value:
    maximum_value = b
if c > maximum_value:
    maximum_value = c

print(maximum_value)
::elab:endcode

::elab:begintest hint="-"
1
2
3
::elab:endtest

::elab:begintest hint="-"
-1
0
-999
::elab:endtest

::elab:begintest hint="-"
-1
-2
-3
::elab:endtest

::elab:begintest hint="-"
50
9
7
::elab:endtest

::elab:begintest hint="-"
0
0
0
::elab:endtest