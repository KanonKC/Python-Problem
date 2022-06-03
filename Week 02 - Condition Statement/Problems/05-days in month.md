# Days In Month

เขียนโปรแกรมที่รับค่าเป็นเดือน และปีพุทธศักราช แล้วบอกว่าในเดือนๆนั้นของปีนั้นจะมีจำนวนวันทั้งหมดกี่วัน

**ข้อมูลนำเข้า**  
บรรทัดที่ 1 เป็นตัวเลขจำนวนเต็ม แทนลำดับเดือนของปีนั้นๆ  
บรรทัดที่ 2 เป็นตัวเลขจำนวนเต็ม แทนปีพุทธศักราช

**ข้อมูลส่งออก**  
ตอบเป็นเพียงตัวเลขว่าจะมีจำนวนวันทั้งหมดกี่วัน

**คำใบ้**  
ปัญหาของข้อนี้อยู่ที่เดือนกุมภาพันธ์ ซึ่งโดยปกติแล้วเดือนนี้จะมีจำนวนวันทั้งหมด 28 วันยกเว้นปีที่เป็น **ปีอธิกสุรทิน (Leap Year)** ซึ่งจะมี 29 แทน โดยเราสามารถเช็คได้โดย ปีอธิกสุรทิน คือปีที่ `ปี ค.ศ. หารด้วย 4 ลงตัว แต่หาร 100 ไม่ลงตัว ยกเว้นปีที่หาร 400 ลงตัว`

## Example 1
<pre class="output">
m: _10_
y: _2556_
31
</pre>

## Example 2
<pre class="output">
m: _4_
y: _2557_
30
</pre>

## Example 3
<pre class="output">
m: _2_
y: _2557_ 
28
</pre>

## Example 4
<pre class="output">
m: _2_
y: _2547_
29
</pre>

::elab:begincode blank=True
m = int(input("m: "))
y = int(input("y: "))
y-=543
if m == 2:
    if (y%4==0 and y%100!=0) or y%400==0:
        print("29")
    else:
        print("28")
elif m in [4,6,9,11]:
    print("30")
else:
    print("31")
::elab:endcode

::elab:begintest hint="-"
7
2537
::elab:endtest
::elab:begintest hint="-"
8
2555
::elab:endtest
::elab:begintest hint="-"
2
2443
::elab:endtest
::elab:begintest hint="-"
2
2543
::elab:endtest
::elab:begintest hint="-"
2
2563
::elab:endtest
::elab:begintest hint="-"
2
2574
::elab:endtest
::elab:begintest hint="-"
7
2567
::elab:endtest
::elab:begintest hint="-"
11
2384
::elab:endtest
::elab:begintest hint="-"
1
2947
::elab:endtest