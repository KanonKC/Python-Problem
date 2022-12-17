# Power Of Two

จงเขียนโปรแกรมที่รับจำนวนเต็มบวกค่าหนึ่งเข้ามา และตอบว่าจำนวนนั้นเป็นจำนวนที่สามารถเขียนได้ในรูป 2^n หรือไม่ (เช่น 1, 2, 4, 8, 16, ...)

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็นจำนวนเต็มบวก **n** โดยที่ `1 ≤ n ≤ 100,000,000`

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ว่าจำนวน n นั้นเกิดจาก 2 คูณกันอย่างเดียวหรือไม่

**คำใบ้:** อาจจะดูเหมือนว่าโจทย์ข้อนี้จำเป็นต้องใช้เรื่อง Loop เข้ามาช่วย แต่จริงๆเราสามารถใช้เพียง `if-else` ในการแก้ปัญหานี้ได้ โดยใช้ประโยชน์จากข้อมูลที่ว่า `1 ≤ n ≤ 100,000,000`

## Example 1
<pre class="output">
n: _2_
True
</pre>

## Example 2
<pre class="output">
n: _14_
False
</pre>

## Example 3
<pre class="output">
n: _1024_
True
</pre>

::elab:begincode blank=True
n = int(input("n: "))

if 2**27 % n == 0:
    print(True)
else:
    print(False)
::elab:endcode

::elab:begintest hint="-"
2
::elab:endtest
::elab:begintest hint="-"
14
::elab:endtest
::elab:begintest hint="-"
1024
::elab:endtest
::elab:begintest hint="-"
274
::elab:endtest
::elab:begintest hint="-"
8192
::elab:endtest
::elab:begintest hint="-"
131072
::elab:endtest
::elab:begintest hint="-"
27944392
::elab:endtest
::elab:begintest hint="-"
28385
::elab:endtest
::elab:begintest hint="-"
33554432
::elab:endtest
::elab:begintest hint="-"
1
::elab:endtest