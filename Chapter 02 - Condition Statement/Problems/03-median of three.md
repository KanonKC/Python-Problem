# Median Of Three

Median(ค่ามัธยฐาน) คือค่ากลางของข้อมูล สมมุติว่าเรามีจำนวน 3 จำนวน ค่ามัธยฐานก็คือจำนวนที่ไม่ได้เป็นค่ามากสุด และน้อยสุด นั่นเอง

<img src="https://www.codingem.com/wp-content/uploads/2021/11/median-in-Python-1024x457.png" width="500px">

จงเขียนโปรแกรมที่รับจำนวนเต็ม 3 จำนวน และหาค่ามัธยฐานของชุดข้อมูลนี้

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 3 บรรทัด โดยแต่ละบรรทัดเป็นจำนวนเต็ม

<u>ข้อมูลส่งออก</u>  
แสดงค่ามัธยฐานของชุดข้อมูลนี้

## Example 1
<pre class="output">
Enter 3 Numbers:
\#1: _1_
\#2: _2_
\#3: _3_
Median is 2
</pre>

## Example 2
<pre class="output">
Enter 3 Numbers:
\#1: _6_
\#2: _1_
\#3: _5_
Median is 5
</pre>

::elab:begincode blank=True
print("Enter 3 Numbers:")
a = int(input("#1: "))
b = int(input("#2: "))
c = int(input("#3: "))

if (a >= b and a <= c) or (a >= c and a <= b):
    print(f"Median is {a}")
elif (b >= a and b <= c) or (b >= c and b <= a):
    print(f"Median is {b}")
else:
    print(f"Median is {c}")
::elab:endcode

::elab:begintest hint="-"
1
2
3
::elab:endtest

::elab:begintest hint="-"
6
1
5
::elab:endtest

::elab:begintest hint="-"
4
2
6
::elab:endtest

::elab:begintest hint="-"
-1
5
3
::elab:endtest

::elab:begintest hint="-"
-10
-5
-7
::elab:endtest

::elab:begintest hint="-"
-452
-10
-9999
::elab:endtest