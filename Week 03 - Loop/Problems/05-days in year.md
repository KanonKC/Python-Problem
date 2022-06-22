# Days in Year

เขียนโปรแกรมที่รับค่า วัน เดือน และปี(พ.ศ.) ให้แสดงคำตอบว่าวันนั้นคือวันที่เท่าไหร่ของปีแล้ว

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 3 บรรทัด รับค่า วัน เดือน และปี(พ.ศ.) ตามลำดับ โดยทุกค่าเป็นจำนวนเต็มบวกทั้งหมด

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดงคำตอบว่าวันนั้นคือวันที่เท่าไหร่ของปีแล้ว

## Example 1
<pre class="output">
D: _1_
M: _1_
Y: _2565_
1
</pre>

## Example 2
<pre class="output">
D: _6_
M: _5_
Y: _2565_
126
</pre>

## Example 3
<pre class="output">
D: _31_
M: _12_
Y: _2562_
365
</pre>

## Example 4
<pre class="output">
D: _31_
M: _12_
Y: _2563_
366
</pre>

::elab:begincode blank=True
d = int(input("D: "))
m = int(input("M: "))
y = int(input("Y: "))
y -= 543
total = d
for i in range(1,m):
    if i == 2:
        if (y%4 == 0 and y%100 != 0) or y%400==0:
            total += 29
        else:
            total += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        total += 30
    else:
        total += 31
print(total)
::elab:endcode

::elab:begintest hint="-"
1
1
2563
::elab:endtest
::elab:begintest hint="-"
28
2
2555
::elab:endtest
::elab:begintest hint="-"
3
12
2556
::elab:endtest
::elab:begintest hint="-"
7
6
2543
::elab:endtest
::elab:begintest hint="-"
12
12
2443
::elab:endtest
::elab:begintest hint="-"
1
5
2574
::elab:endtest
::elab:begintest hint="-"
2
2
2556
::elab:endtest
::elab:begintest hint="-"
7
7
2557
::elab:endtest