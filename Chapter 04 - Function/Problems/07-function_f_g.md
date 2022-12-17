# Function F, G

***Recommend**: ก่อนจะลงมือจะทำโจทย์ข้อนี้ควรจะเคยทำ `Function F` มาก่อน*  

กำหนดฟังก์ขัน `f(x), g(x,y)` โดยมีเงื่อนไขดังนี้

<img src="https://latex.codecogs.com/gif.latex?%5Cdpi%7B300%7D%20f%28x%29%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%203x-5%20%26%205%20%5Cleq%20x%20%5Cleq%2025%20%5C%5C%205%20%26%20Otherwise%20%5Cend%7Bmatrix%7D%5Cright." width="200px">  

<img src="https://latex.codecogs.com/gif.latex?%5Cdpi%7B300%7D%20g%28x%2Cy%29%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20x&plus;y%20%26%20x%20%3E%200%20%5C%5C%205xy%20%26%20x%20%3C%200%20%5C%5C%201%20%26%20Otherwise%20%5Cend%7Bmatrix%7D%5Cright." width="200px">

เขียนโปรแกรมที่รับค่า x และ y เข้ามา และแสดงผลลัพธ์ที่ได้จาก `f(y) * g(y,x)`

**คำแนะนำ:** สามารถก็อปฟังก์ชัน `f(x)` จากข้อ `Function F` มาใช้ได้เลย

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นจำนวนเต็มทั้งคู่   
**บรรทัดที่ 1** แทนค่า x  
**บรรทัดที่ 2** แทนค่า y

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดงผลลัพธ์ที่ได้จาก `f(y) * g(y,x)`

## Example 1
<pre class="output">
x: _3_
y: _5_
80
</pre>

## Example 2
<pre class="output">
x: _0_
y: _0_
5
</pre>

::elab:begincode blank=True
def f(x):
    if x >= 5 and x <= 25:
        return 3*x - 5
    else:
        return 5

def g(x,y):
    if x > 0:
        return x + y
    elif x < 0:
        return 5*x*y
    else:
        return 1

x = int(input("x: "))
y = int(input("y: "))

print(f(y)*g(y,x))
::elab:endcode

::elab:begintest hint="-"
3
5
::elab:endtest
::elab:begintest hint="-"
0
0
::elab:endtest
::elab:begintest hint="-"
9
-4
::elab:endtest
::elab:begintest hint="-"
19
30
::elab:endtest
::elab:begintest hint="-"
-1
9
::elab:endtest
::elab:begintest hint="-"
-14
-10
::elab:endtest
::elab:begintest hint="-"
-27
13
::elab:endtest
::elab:begintest hint="-"
3
14
::elab:endtest
::elab:begintest hint="-"
-28
-17
::elab:endtest
::elab:begintest hint="-"
0
15
::elab:endtest
::elab:begintest hint="-"
-10
10
::elab:endtest