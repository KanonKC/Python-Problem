# Quadrant

Quadrant หรือจตุภาค เป็นที่สิ่งเอาไว้แบ่งพื้นที่ในกราฟโดยใช้แกน x และแกน y โดยสำหรับพิกัด (x, y) จะสามารถแบ่งได้ดังนี้

- ถ้า x เป็นบวก และ y เป็นบวก จะเป็น **Quadrant 1**
- ถ้า x เป็นลบ และ y เป็นบวก จะเป็น **Quadrant 2**
- ถ้า x เป็นลบ และ y เป็นลบ จะเป็น **Quadrant 3**
- ถ้า x เป็นบวก และ y เป็นลบ จะเป็น **Quadrant 4**

นอกจากนี้จะยังมีกรณีที่พิกัดคาบอยู่บนเส้นของแกน x หรือ y พอดี

- ถ้า x เป็น 0 และ y เป็นบวก จะเป็น **Positive Y-Axis** *(พิกัดอยู่บนแกน y ด้านบวก)*
- ถ้า x เป็น 0 และ y เป็นลบ จะเป็น **Negative Y-Axis** *(พิกัดอยู่บนแกน y ด้านลบ)*
- ถ้า x เป็นลบ และ y เป็น 0 จะเป็น **Negative X-Axis**
- ถ้า x เป็นบวก และ y เป็น 0 จะเป็น **Positive X-Axis**
- ถ้า x เป็น 0 และ y เป็น 0 จะเป็น **Origin** *(จุดกำเนิดของกราฟมีพิกัดเป็น (0, 0))*

<img src="https://www.math.net/img/a/geometry/coordinate-plane/quadrant/signs-of-quadrant.png">

ให้เขียนโปรแกรมที่รับค่าพิกัด (x, y) เข้ามาและตอบกลับไปว่าอยู่ Quadrant ไหนหรืออยู่บนแกนใด โดยคำตอบที่จะแสดงออกมาจะมีทั้งหมด 9 แบบตามตัวอักษรตัวหนาด้านบน (Quadrant 1, Quadrant 2, Quadrant 3, Quadrant 4, Positive Y-Axis, Negative Y-Axis, Negative X-Axis, Positive X-Axis, Origin)

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด โดยที่ทั้งคู่จะเป็นจำนวนจริงใดๆ  
บรรทัดที่ 1 รับค่าพิกัดสำหรับแกน **x**  
บรรทัดที่ 2 รับค่าพิกัดสำหรับแกน **y**

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบว่าพิกัดที่ใส่มาอยู่ Quadrant ไหนหรืออยู่บนแกนใด โดยคำตอบที่จะแสดงออกมาจะมีทั้งหมด 9 แบบตามตัวอักษรตัวหนาด้านบน (Quadrant 1, Quadrant 2, Quadrant 3, Quadrant 4, Positive Y-Axis, Negative Y-Axis, Negative X-Axis, Positive X-Axis, Origin)

## Example 1
<pre class="output">
x: _2_
y: _-3_
Quadrant 4
</pre>

## Example 2
<pre class="output">
x: _-1_
y: _-1_
Quadrant 3
</pre>

## Example 3
<pre class="output">
x: _0_
y: _-1_
Negative Y-Axis
</pre>

## Example 4
<pre class="output">
x: _0_
y: _0_
Origin
</pre>

::elab:begincode blank=True
x = float(input("x: "))
y = float(input("y: "))

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    if y > 0:
        print("Positive Y-Axis")
    else:
        print("Negative Y-Axis")
elif y == 0:
    if x > 0:
        print("Positive X-Axis")
    else:
        print("Negative X-Axis")
elif x > 0:
    if y > 0:
        print("Quadrant 1")
    else:
        print("Quadrant 4")
else:
    if y > 0:
        print("Quadrant 2")
    else:
        print("Quadrant 3")
::elab:endcode

::elab:begintest hint="-"
3.156
5.23
::elab:endtest

::elab:begintest hint="-"
-4.6
2.33
::elab:endtest

::elab:begintest hint="-"
-1.984
-3
::elab:endtest

::elab:begintest hint="-"
86
-11
::elab:endtest

::elab:begintest hint="-"
0
-1
::elab:endtest

::elab:begintest hint="-"
0
10
::elab:endtest

::elab:begintest hint="-"
0
0
::elab:endtest

::elab:begintest hint="-"
1.36
0
::elab:endtest

::elab:begintest hint="-"
-7.36
0
::elab:endtest

::elab:begintest hint="-"
7
7
::elab:endtest