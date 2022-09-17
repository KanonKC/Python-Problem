# Rectangle

เขียนโปรแกรมที่วาดรูปสี่เหลี่ยมผืนผ้าออกมา โดยที่รับค่าความยาว และความสูง

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัดโดยรับเข้ามาเป็นจำนวนเต็มบวกทั้งคู่
บรรทัดที่ 1 รับค่าความ **ยาว** ของสี่เหลี่ยมผืนผ้า  
บรรทัดที่ 2 รับค่าความ **สูง** ของสี่เหลี่ยมผืนผ้า

<u>ข้อมูลส่งออก</u>  
แสดงออกเป็นรูปสี่เหลี่ยมผืนผ้าที่วาดโดยใช้ตัวอักษร `#`

## Example 1
<pre class="output">
_5_
_3_
\#####
\#####
\#####
</pre>

## Example 1
<pre class="output">
_10_
_1_
\##########
</pre>

## Example 1
<pre class="output">
_3_
_3_
\###
\###
\###
</pre>


::elab:begincode blank=True
l = int(input())
h = int(input())

for i in range(h):
    print("#"*l)
::elab:endcode

::elab:begintest hint="-"
20
44
::elab:endtest
::elab:begintest hint="-"
77
61
::elab:endtest
::elab:begintest hint="-"
19
94
::elab:endtest
::elab:begintest hint="-"
19
88
::elab:endtest
::elab:begintest hint="-"
13
30
::elab:endtest
::elab:begintest hint="-"
64
69
::elab:endtest
::elab:begintest hint="-"
19
60
::elab:endtest
::elab:begintest hint="-"
84
10
::elab:endtest
::elab:begintest hint="-"
61
12
::elab:endtest
::elab:begintest hint="-"
58
67
::elab:endtest