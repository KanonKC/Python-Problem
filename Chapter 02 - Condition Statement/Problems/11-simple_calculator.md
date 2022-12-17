# Simple Calculator

ให้นิสิตสร้างเครื่องคิดเลยที่รับตัวเลข 2 จำนวน x และ y รับเครื่องหมายที่ใช้ในการคำนวณซึ่งมีให้เลือก5 ชนิด คือ + - *
/ และ % หากใส่เครื่องหมายไม่ตรงกับ 5 ชนิดนี้ ให้แสดงว่า Unknown Operator ออกทางหน้าจอ โดยทศนิยมให้แสดงเพียง2ตำแหน่งเมื่อเป็นการหาร นอกจากนั้นแสดงค่าเป็นจำนวนเต็ม (โดยค่า x y ที่รับมานั้น เป็นจำนวนเต็ม)

## Example 1
<pre class="output">
x: _3_
Operator: _+_
y: _2_
5
</pre>

## Example 2
<pre class="output">
x: _10_
Operator: _-_
y: _20_
-10
</pre>

## Example 3
<pre class="output">
x: _5_
Operator: _*_
y: _3_
15
</pre>

Example4
--------
<pre class="output">
x: _4_
Operator: _/_
y: _3_
1.33
</pre>

Example5
---------
<pre class="output">
x: _4_
Operator: _%_
y: _3_
1
</pre>

Example6
---------
<pre class="output">
x: _4_
Operator: _._
y: _3_
Unknown Operator
</pre>

::elab:begincode blank=True
x = int(input("x: "))
oprt = input("Operator: ")
y = int(input("y: "))

if(oprt=="+"):
  print(x+y)
elif(oprt=="-"):
  print(x-y)
elif(oprt=="*"):
  print(x*y)
elif(oprt=="/"):
  print(f"{x/y:.2f}")
elif(oprt=="%"):
  print(x%y)
else:
  print("Unknown Operator")
::elab:endcode

::elab:begintest hint="test1"
3
+
2
::elab:endtest

::elab:begintest hint="test2"
10
-
20
::elab:endtest

::elab:begintest hint="test3"
5
*
3
::elab:endtest

::elab:begintest hint="test4"
4
/
3
::elab:endtest

::elab:begintest hint="test5"
4
%
3
::elab:endtest

::elab:begintest hint="test6"
4
.
3
::elab:endtest