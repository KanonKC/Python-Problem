# Greatest Common Divisor

เขียนโปรแกรมที่ใช้หา หารร่วมมาก(ห.ร.ม) ของจำนวนเต็ม 2 จำนวน

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นจำนวนเต็มทั้งคู่

<u>ข้อมูลส่งออก</u>  
แสดงตัวหารร่วมมาก(ห.ร.ม) ของจำนวนเต็ม 2 จำนวน

## Example 1
<pre class="output">
A: _3_
B: _2_
1
</pre>

## Example 2
<pre class="output">
A: _3_
B: _2_
1
</pre>

::elab:begincode blank=True
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

a = int(input("A: "))
b = int(input("B: "))

print(gcd(a,b))
::elab:endcode

::elab:begintest hint="-"
14
48

::elab:begintest hint="-"
3
2

::elab:endtest
::elab:begintest hint="-"
50
50

::elab:endtest
::elab:begintest hint="-"
30
60

::elab:endtest
::elab:begintest hint="-"
60
30

::elab:endtest