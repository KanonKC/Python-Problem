# Factorial

หากเรามีจำนวนเต็มบวกจำนวนหนึ่ง Factorial ของจำนวนนั้นก็ึคือผลคูณของจำนวนเต็มทั้งหมดตั้งแต่ตัวเอง ไปจนถึง 1 (ในทางคณิตศาสตร์จะได้สัญลักษณ์ `!` แทน Factorial) เช่น `5! = 5 x 4 x 3 x 2 x 1 = 120` สำหรับ `0! = 1` (เป็นสมบัติพิเสษ)

ให้เขียนโปรแกรมที่รับจำนวนเต็มบวก และแสดงผลของของ Factorial ของค่านั้น

**ข้อมูลนำเข้า**  
มีบรรทัดเดียว เป็นจำนวนเต็มที่*ไม่ใช่*จำนวนเต็มลบ **n**

**ข้อมูลส่งออก**  
แสดงผลของของ Factorial ของค่า n

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
n = int(input("n: "))

res = 1
for i in range(1,n+1):
    res *= i

if n == 0:
    print(1)
else:
    print(res)
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