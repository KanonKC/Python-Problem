# Factorial (Recursive)

หากเรามีจำนวนเต็มบวกจำนวนหนึ่ง Factorial ของจำนวนนั้นก็ึคือผลคูณของจำนวนเต็มทั้งหมดตั้งแต่ตัวเอง ไปจนถึง 1 (ในทางคณิตศาสตร์จะได้สัญลักษณ์ `!` แทน Factorial) เช่น `5! = 5 x 4 x 3 x 2 x 1 = 120` สำหรับ `0! = 1` (เป็นสมบัติพิเสษ)

ให้เขียนโปรแกรมที่รับจำนวนเต็มบวก และแสดงผลของของ Factorial ของค่านั้น

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มที่*ไม่ใช่*จำนวนเต็มลบ **n**

<u>ข้อมูลส่งออก</u>  
แสดงผลของของ Factorial ของค่า n

<u>ข้อกำหนดเพิ่มเติม</u>  
ในโปรแกรมที่ส่งจะต้องมีการประกาศฟังก์ชัน `fac(n)` ที่เขียนในรูปแบบ Recursive  

**Parameter**  
`n` เป็น `int` แทนค่า Factorial ที่จะต้องการจะหา  

**Return**  
`int` แทนค่า Factorial ของ `n`

## Example 1
<pre class="output">
n: _0_
1
</pre>

## Example 2
<pre class="output">
n: _5_
120
</pre>

## Example 3
<pre class="output">
n: _10_
3628800
</pre>

::elab:begincode blank=True
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(int(input("n: "))))
::elab:endcode

::elab:begintest hint="-"
0
::elab:endtest
::elab:begintest hint="-"
1
::elab:endtest
::elab:begintest hint="-"
2
::elab:endtest
::elab:begintest hint="-"
5
::elab:endtest
::elab:begintest hint="-"
10
::elab:endtest
::elab:begintest hint="-"
8
::elab:endtest
::elab:begintest hint="-"
12
::elab:endtest
::elab:begintest hint="-"
4
::elab:endtest
::elab:begintest hint="-"
3
::elab:endtest