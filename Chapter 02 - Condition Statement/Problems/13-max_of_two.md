# Max of Two

เขียนโปรแกรมที่หาค่าที่มากที่สุดของจำนวนทั้ง 2 ตัวนี้

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นจำนวนเต็มแทนทั้งคู่

<u>ข้อมูลส่งออก</u>  
จำนวนที่มีค่ามากที่สุด

## Example 1
<pre class="output">
_1_
_2_
2
</pre>

## Example 2
<pre class="output">
_0_
_-1_
0
</pre>

::elab:begincode blank=True
a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)
::elab:endcode

::elab:begintest hint="-"
1
2
::elab:endtest

::elab:begintest hint="-"
0
-1
::elab:endtest

::elab:begintest hint="-"
-1
-2
::elab:endtest

::elab:begintest hint="-"
-5
7
::elab:endtest

::elab:begintest hint="-"
0
0
::elab:endtest