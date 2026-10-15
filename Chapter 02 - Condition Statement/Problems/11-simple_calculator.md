# Simple Calculator

ให้นิสิตสร้างเครื่องคิดเลยที่รับตัวเลข 2 จำนวน x และ y รับเครื่องหมายที่ใช้ในการคำนวณซึ่งมีให้เลือก5 ชนิด คือ + - *
/ และ % หากใส่เครื่องหมายไม่ตรงกับ 5 ชนิดนี้ ให้แสดงว่า Unknown Operator ออกทางหน้าจอ โดยทศนิยมให้แสดงเพียง2ตำแหน่งเมื่อเป็นการหาร นอกจากนั้นแสดงค่าเป็นจำนวนเต็ม (โดยค่า x y ที่รับมานั้น เป็นจำนวนเต็ม)

::elab:begincode blank=True
x = int(input())
oprt = input()
y = int(input())

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