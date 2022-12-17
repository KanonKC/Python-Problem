# Function F

กำหนดฟังก์ขัน `f(x)` โดยมีเงื่อนไขดังนี้

<img src="https://latex.codecogs.com/gif.latex?%5Cdpi%7B300%7D%20f%28x%29%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%203x-5%20%26%205%20%5Cleq%20x%20%5Cleq%2025%20%5C%5C%205%20%26%20Otherwise%20%5Cend%7Bmatrix%7D%5Cright." width="200px">

เขียนโปรแกรมที่รับค่า x เข้ามา และแสดงผลลัพธ์ที่ได้จาก `f(x) + f(2x)`

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับค่า x เป็นจำนวนเต็ม

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดงผลลัพธ์ที่ได้จาก `f(x) + f(2x)`

## Example 1
<pre class="output">
x: _4_
34
</pre>

## Example 2
<pre class="output">
x: _5_
55
</pre>

::elab:begincode blank=True
def f(x):
    if x >= 5 and x <= 25:
        return 3*x - 5
    else:
        return 5

x = int(input("x: "))
print(f(x) + f(2*x))
::elab:endcode

::elab:begintest hint="-"
25
::elab:endtest
::elab:begintest hint="-"
-2
::elab:endtest
::elab:begintest hint="-"
24
::elab:endtest
::elab:begintest hint="-"
4
::elab:endtest
::elab:begintest hint="-"
1
::elab:endtest
::elab:begintest hint="-"
25
::elab:endtest
::elab:begintest hint="-"
2
::elab:endtest
::elab:begintest hint="-"
19
::elab:endtest
::elab:begintest hint="-"
12
::elab:endtest
::elab:begintest hint="-"
-18
::elab:endtest