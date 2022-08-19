# UNIX Timestamp

***Recommend**: ก่อนจะลงมือจะทำโจทย์ข้อนี้ควรจะเคยทำ [days\_in\_year](https://elabsheet.org/elab/taskpads/show/fulvny8ila/) มาก่อน*

**UNIX Timestamp** คือเวลาที่บวก 1 เพิ่มทุกๆวินาที โดยเป็นตัวเลขที่เริ่มนับตั้งแต่วินาทีที่ 00:00:00 ของวันพฤหัสบดี วันที่ 1 มกราคม ค.ศ.1970 เป็นตันมาตามเวลาสากล หรืออาจจะสรุปให้เข้าใจง่ายๆก็คือ "เวลาในหน่วยวินาที ที่เริ่มนับตั้งแต่ 01/01/1970" นั่นเอง  

ในโจทย์นี้ข้อนี้เราจะรับค่า วัน/เดือน/ปี ในวลานึง(ชั่วโมง/นาที/วินาที) และให้แสดงผลลัพธ์เป็น Timestamp สำหรับเวลาขณะนั้น  

สามารถตรวจสอบ Timestamp ได้ [ที่ลิงก์นี้](https://www.unixtimestamp.com/) (ดูที่เวลา GMT)

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 6 บรรทัด แต่ละบรรทัดเป็นจำนวนเต็มบวกทั้งหมด  
**บรรทัดที่ 1** รับค่า **D** แทนวันที่ที่ต้องการทดสอบ โดยที่ 1 ≤ D ≤ 31  
**บรรทัดที่ 2** รับค่า **M** แทนเดือนที่ต้องการทดสอบ โดยที่ 1 ≤ M ≤ 12  
**บรรทัดที่ 3** รับค่า **Y** แทนปี ค.ศ. ที่ต้องการทดสอบ โดยที่ 1970 ≤ Y ≤ 3000  
**บรรทัดที่ 4** รับค่า **h** แทนชั่วโมงที่ต้องการทดสอบ โดยที่ 0 ≤ h ≤ 60  
**บรรทัดที่ 5** รับค่า **m** แทนนาทีที่ต้องการทดสอบ โดยที่ 0 ≤ m ≤ 60  
**บรรทัดที่ 6** รับค่า **s** แทนวินาทีที่ต้องการทดสอบ โดยที่ 0 ≤ s ≤ 60  

<u>ข้อมูลส่งออก</u>  
แสดงค่า UNIX Timestamp ของเวลาดังกล่าว ในหน่วยวินาที

## Example 1
<pre class="output">
Date: _1_
Month: _1_
Year: _1970_
Hour: _0_
Minute: _0_
Second: _0_
0
</pre>

## Example 2
<pre class="output">
Date: _1_
Month: _1_
Year: _1970_
Hour: _0_
Minute: _1_
Second: _40_
100
</pre>

## Example 3
<pre class="output">
Date: _19_
Month: _8_
Year: _2022_
Hour: _20_
Minute: _43_
Second: _38_
1660941818
</pre>

::elab:begincode blank=True
def isLeap(y):
    return (y%4 == 0 and y%100 != 0) or y%400==0

d = int(input("Date: "))
m = int(input("Month: "))
y = int(input("Year: "))

h = int(input("Hour: "))
mn = int(input("Minute: "))
s = int(input("Second: "))

total = d
for i in range(1,m):
    if i == 2:
        if isLeap(y):
            total += 29
        else:
            total += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        total += 30
    else:
        total += 31

for i in range(1970,y):
    if isLeap(i):
        total += 366
    else:
        total += 365

total = ((total-1) * 86400) + (h*3600) + (mn*60) + s

print(total)
::elab:endcode

::elab:begintest hint="-"
1
1
1970
0
0
0
::elab:endtest
::elab:begintest hint="-"
1
1
1970
0
1
40
::elab:endtest
::elab:begintest hint="-"
19
8
2022
20
43
38
::elab:endtest
::elab:begintest hint="-"
11
12
1999
44
26
15
::elab:endtest
::elab:begintest hint="-"
22
4
2519
6
41
35
::elab:endtest
::elab:begintest hint="-"
20
5
2596
58
1
12
::elab:endtest
::elab:begintest hint="-"
3
4
2996
10
23
58
::elab:endtest
::elab:begintest hint="-"
25
1
2490
1
14
46
::elab:endtest
::elab:begintest hint="-"
7
10
2003
38
34
14
::elab:endtest
::elab:begintest hint="-"
31
5
2184
39
28
1
::elab:endtest