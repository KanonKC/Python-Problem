# Quotient & Remainder

Quotient = ผลจากการหาร
Remainder = เศษจากการหาร

ในข้อนี้เราจะมาโฟกัสที่เรื่องการหารกัน โดยเราจะรับจำนวนเข้ามา 2 ตัว จากนั้นคำนวณว่า หากเรานำเลขตัวแรกตั้ง และนำตัวที่สองมาหาร เราจะได้ผลจากการหารเท่าไหร่ และเหลือเศษเท่าไหร่

<img src="https://cdn1.byjus.com/wp-content/uploads/2020/01/maths-division-questions-for-kids-6.png" width="500">

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรททัด เป็นจำนวนเต็มทั้งคู่

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดงทั้งผลลัพธ์ และผลหารให้เหมือนกับตัวอย่างข้างล่าง


## Example 1
<pre class="output">
Dividend: _359_
Divisor: _6_
Quotient = 59, Remainder = 5
</pre>

Dividend = ตัวตั้ง, Divisor = ตัวหาร  

## Example 2
<pre class="output">
Dividend: _100_
Divisor: _10_
Quotient = 10, Remainder = 0
</pre>

100 หารด้วย 10 ลงตัว จึงไม่มีเศษเหลือ

## Example 3
<pre class="output">
Dividend: _2_
Divisor: _7_
Quotient = 0, Remainder = 2
</pre>

เนื่องจาก 2 มีค่าน้อยกว่า 7 เลยหารไม่ได้ และกลายเป็นเศษไป

**ข้อสังเกตุ**  
1\) สำหรับการแสดงผล จะยังเหมือนกับข้อก่อนหน้า เพียงแค่แสดง 2 ค่าในบรรทัดเดียวแทน  
2\) สังเกตุที่ตอนรับค่าตัวเลขเข้ามา มีข้อความแสดงมาจากโปรแกรมด้วย (พวก Dividend, Divisor)  
3\) ข้อความจากข้อที่สอง **มีเคาะ Spacebar ก่อนตัวเลข**  

::elab:begincode blank=True
a = int(input("Dividend: "))
b = int(input("Divisor: "))

quotient = a // b
remainder = a % b

print(f"Quotient = {quotient}, Remainder = {remainder}")
::elab:endcode

::elab:begintest hint="-"
359
6
::elab:endtest

::elab:begintest hint="-"
100
10
::elab:endtest

::elab:begintest hint="-"
2
7
::elab:endtest

::elab:begintest hint="-"
410670
729962
::elab:endtest
::elab:begintest hint="-"
9999999
999
::elab:endtest
::elab:begintest hint="-"
8888888
88
::elab:endtest
::elab:begintest hint="-"
770509
146156
::elab:endtest
::elab:begintest hint="-"
668945
417285
::elab:endtest
::elab:begintest hint="-"
598749
719107
::elab:endtest
::elab:begintest hint="-"
360505
748634
::elab:endtest