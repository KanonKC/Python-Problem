# Fibonacci (Recursive)

**ลำดับฟีโบนักชี (Fibonacci sequence)** คือ ลำดับ Fn ซึ่ง F1 = 1, F2 = 1 และ Fn = Fn−1 + Fn− 2 เมื่อ n ≥ 3 โดยเรียกแต่ละพจน์ของลำดับฟีโบนักชีว่า จำนวนฟีโบนักชี (Fibonacci number) ซึ่งได้แก่ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, … จะเห็นว่าแต่ละพจน์ของลำดับฟีโบนักชี ได้จากผลบวกของสองพจน์ก่อนหน้า

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับค่าเข้ามาเป็นจำนวนเต็มบวกแทนลำดับของฟีโบนักชี **n** โดยที่ 1 ≤ n ≤ 30

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์เป็นจำนวนฟีโบนักชีลำดับที่ n (ตามลำดับที่ใส่เข้ามา)

<u>ข้อกำหนดเพิ่มเติม</u>  
ในโปรแกรมที่ส่งจะต้องมีการประกาศฟังก์ชัน `fib(n)` ที่เขียนในรูปแบบ Recursive  

**Parameter**  
`n` เป็น `int` แทนลำดับของ Fibonacci ที่จะต้องการจะหา  

**Return**  
`int` แทนค่า Fibonacci ในลำดับที่ `n`

## Example 1
<pre class="output">
n: _1_
1
</pre>

## Example 2
<pre class="output">
n: _2_
1
</pre>

## Example 3
<pre class="output">
n: _20_
6765
</pre>

## Example 4
<pre class="output">
n: _25_
75025
</pre>

::elab:begincode blank=True
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(int(input("n: "))))
::elab:endcode

::elab:begintest hint="-"
27
::elab:endtest
::elab:begintest hint="-"
17
::elab:endtest
::elab:begintest hint="-"
11
::elab:endtest
::elab:begintest hint="-"
30
::elab:endtest
::elab:begintest hint="-"
6
::elab:endtest
::elab:begintest hint="-"
19
::elab:endtest
::elab:begintest hint="-"
3
::elab:endtest
::elab:begintest hint="-"
24
::elab:endtest
::elab:begintest hint="-"
2
::elab:endtest
::elab:begintest hint="-"
1
::elab:endtest