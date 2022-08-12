# Function F

กำหนด Function f(x) โดยมีเงื่อนไขดังนี้

<img src="https://cdn.discordapp.com/attachments/897797648130654258/1002786255404290149/image.png" width="200px">

เขียนโปรแกรมที่รับค่า x เข้ามา และแสดงผลลัพธ์ที่ได้จาก f(x) + f(2x)

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับค่า x เป็นจำนวนจริง

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดงผลลัพธ์ที่ได้จาก f(x) + f(2x)

## Example 1
<pre class="output">
_4_
34
</pre>

## Example 2
<pre class="output">
_5_
55
</pre>

::elab:begincode blank=True
def f(x):
    if x >= 5 and x <= 25:
        return 3*x + 5
    else:
        return 5

x = float(input())
print(f(x)+f(2*x))
::elab:endcode

::elab:begintest hint="-"
25.593
::elab:endtest
::elab:begintest hint="-"
-2.822
::elab:endtest
::elab:begintest hint="-"
24.92
::elab:endtest
::elab:begintest hint="-"
4.123
::elab:endtest
::elab:begintest hint="-"
4.905
::elab:endtest
::elab:begintest hint="-"
25.224
::elab:endtest
::elab:begintest hint="-"
2.91
::elab:endtest
::elab:begintest hint="-"
19.925
::elab:endtest
::elab:begintest hint="-"
12.377
::elab:endtest
::elab:begintest hint="-"
-18.59
::elab:endtest