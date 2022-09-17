# Twin Prime

**Twin Prime** คือ คู่ของจำนวนเฉพาะที่ทั้งสองจำนวนมีค่าห่างกันแค่ 2 (ถ้า P และ P+2 เป็นจำนวนเฉพาะทั้งคู่ ก็แสดงว่า P,P+2 เป็น Twin Prime)

เขียนโปรแกรมที่รับค่าจำนวนเต็มบวก 1 ตัว และให้หาคู่ Twin Prime ที่ใกล้ที่สุด และมีค่า*มากกว่า*ตัวเองทั้งคู่

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็นจำนวนเต็มบวก n

<u>ข้อมูลส่งออก</u>  
หาคู่ Twin Prime ที่ใกล้ที่สุด และมีค่ามากกว่า n ทั้งคู่

## Example 1
<pre class="output">
_4_
5, 7
</pre>

## Example 2
<pre class="output">
_5_
11, 13
</pre>

## Example 3
<pre class="output">
_200_
227, 229
</pre>

::elab:begincode blank=True
def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n = int(input()) + 1

while not (isPrime(n) and isPrime(n+2)):
    n += 1

print(f"{n}, {n+2}")
::elab:endcode

::elab:begintest hint="-"
4
::elab:endtest
::elab:begintest hint="-"
5
::elab:endtest
::elab:begintest hint="-"
200
::elab:endtest
::elab:begintest hint="-"
954782
::elab:endtest
::elab:begintest hint="-"
64574
::elab:endtest
::elab:begintest hint="-"
208043
::elab:endtest
::elab:begintest hint="-"
397836
::elab:endtest
::elab:begintest hint="-"
904895
::elab:endtest
::elab:begintest hint="-"
68558
::elab:endtest
::elab:begintest hint="-"
252519
::elab:endtest