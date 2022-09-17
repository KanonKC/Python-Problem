# Parallel  
 
รับค่าพิกัด x1,y1,x2,y2 ของเส้นตรงเส้นที่ 1 และรับค่าความชัน m ของเส้นตรงเส้นที่ 2  
จากนั้นให้ตอบว่าเส้นตรงทั้ง 2 นั้นขนานกันหรือไม่

<img style="width:300px; " src="https://cdn.discordapp.com/attachments/1005665610614714380/1005665652134121655/image0.jpg">

<u>ข้อมูลนำเข้า</u>  
มี 5 บรรทัด เป็นจำนวนเต็ม x1,y1,x2,y2 และจำนวนจริง m

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบว่าเส้นตรงทั้ง 2 ขนานกันหรือไม่

** ภายในโปรแกรมต้องมีฟังก์ชันดังต่อไปนี้ **

* <span style="color:red;"> `findSlope(x1,y1,x2,y2)` </span> สำหรับรับค่า x1,y1,x2,y2 จากนั้น**คืนค่าความชันของเส้นตรงเส้นที่ 1**
* <span style="color:red;"> `isParallel(m1,m2)` </span> สำหรับรับค่าความชันของเส้นตรงทั้ง 2 เส้น จากนั้น**แสดงผลว่า Parallel** หากเส้นตรงทั้ง 2 ขนานกัน หรือ**แสดงผลว่า Not parallel** หากเส้นตรงทั้ง 2 ไม่ขนานกัน

Example 1
---------
<pre class="output">
Input x1: _1_
Input y1: _2_
Input x2: _3_
Input y2: _4_
Input m: _1_
Parallel
</pre>

Example 2
---------
<pre class="output">
Input x1: _2_
Input y1: _0_
Input x2: _3_
Input y2: _5_
Input m: _2_
Not parallel
</pre>


::elab:begincode blank=True

def findSlope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

def isParallel(m1,m2):
    if(m1==m2):
        print('Parallel')
    else:
        print('Not parallel')

x1 = int(input("Input x1: "))
y1 = int(input("Input y1: "))
x2 = int(input("Input x2: "))
y2 = int(input("Input y2: "))
m2 = float(input("Input m: "))

m1 = findSlope(x1,y1,x2,y2)
isParallel(m1,m2)
::elab:endcode

::elab:begincode hidden=True
check = input()
if check == '01':
    print(findSlope(1,2,3,4))
elif check == '02':
    isParallel(5,6)
::elab:endcode

::elab:begintest hint="findSlope(x1,y1,x2,y2) defined?"
1
2
3
4
1
01
::elab:endtest

::elab:begintest hint="isParallel(m1,m2) defined?"
1
2
3
4
1
02
::elab:endtest

::elab:begintest hint="test 1"
1
2
3
4
1

::elab:endtest

::elab:begintest hint="test 2"
2
0
3
5
2

::elab:endtest

::elab:begintest
3
2
5
-4
-3

::elab:endtest

::elab:begintest
-1
-2
-5
4
-1.5

::elab:endtest

::elab:begintest
-1
-2
-5
4
6

::elab:endtest