# Plus

เขียนโปรแกรมที่รับจำนวนเต็ม 2 จำนวนเข้ามา จากนั้นคำนวณผลบวกออกมา

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นจำนวนเต็มทั้งคู่

<u>ข้อมูลส่งออก</u>  
ผลบวกของ 2 จำนวนที่รับเข้ามา

## Example 1
<pre class="output">
_1_
_1_
2
</pre>

ตรงนี้จะเป็นตัวอย่างหน้าต่างตอนเรารันโปรแกรมจริงๆ โดยที่ตรงไหนที่เป็น **สีแดง** จะเป็นสิ่งที่เราเป็นคนพิมพ์ใส่ไปเอง ส่วนตรงที่เป็น **สีดำ** จะต้องออกมาเองจากโปรแกรมของเรา

## Example 2
<pre class="output">
_5_
_0_
5
</pre>

## Example 3
<pre class="output">
_7_
_5_
12
</pre>

::elab:begincode blank=True
a = int(input())
b = int(input())

print(a+b)
::elab:endcode

::elab:begintest hint="-"
1
1
::elab:endtest
::elab:begintest hint="-"
5
0
::elab:endtest
::elab:begintest hint="-"
7
5
::elab:endtest
::elab:begintest hint="-"
797197
444884
::elab:endtest
::elab:begintest hint="-"
189562
763394
::elab:endtest
::elab:begintest hint="-"
548026
775019
::elab:endtest
::elab:begintest hint="-"
383836
962075
::elab:endtest
::elab:begintest hint="-"
117060
533534
::elab:endtest
::elab:begintest hint="-"
476162
209806
::elab:endtest
::elab:begintest hint="-"
443431
420817
::elab:endtest