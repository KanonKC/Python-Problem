# Temperature

หน่วยการวัดค่าความร้อนหรืออุณหภูมิโดยทั่วไปมี 4 หน่วยได้แก่

1) องศาเซลเซียสเขียนย่อว่า °C (Celsius)
2) เคลวินเขียนย่อ K (Kelvin)
3) องศาฟาเรนไฮต์เขียนย่อว่า °F (Fahrenheit)
4) องศา Réaumur (เขียนย่อเป็น °Ré, ° Re)

โดยเราสามารถแปลงหน่วยของแต่ละหน่วยได้ตามสูตรดังนี้

![](https://t4.ftcdn.net/jpg/04/53/04/03/360_F_453040381_6tmWKvQAnyul9ZKCLvr7ITiktPHwzmbX.webp)

เขียนโปรแกรมที่รับอุณหภูมิในหน่วยใดๆ ก็ได้ แล้วแสดงผลอุณหภูมิในหน่วยอื่นๆ ตามที่กำหนด

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด  
**บรรทัดที่ 1** รับเป็นข้อความที่เป็นจำนวนอุณหภูมิ และหน่วยของมัน (ดูตัวอย่างด้านล่างประกอบ)  
**บรรทัดที่ 2** รับเป็นตัวอักษรแทนหน่วยที่ต้องการแปลง (ได้แก่ C, K, F, R)  

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ของอุณหภูมิที่แปลงแล้ว โดยแสดงทศนิยม 2 ตำแหน่ง

## Example 1
<pre class="output">
Enter the temperature: _30 C_
Enter the unit to be converted: _K_
303.15 K
</pre>

## Example 2
<pre class="output">
Enter the temperature: _80 F_
Enter the unit to be converted: _C_
26.67 C
</pre>

## Example 3
<pre class="output">
Enter the temperature: _50 F_
Enter the unit to be converted: _R_
8.00 R
</pre>

::elab:begincode blank=True
[temp,unit] = input("Enter the temperature: ").split()
targetUnit = input("Enter the unit to be converted: ")

temp = float(temp)

if unit == "C":
    c = temp
elif unit == "F":
    c = (temp - 32) * 5/9
elif unit == "K":
    c = temp - 273.15
elif unit == "R":
    c = 5/4 * temp

if targetUnit == "C":
    print(f"{(c):.2f} C")
elif targetUnit == "F":
    print(f"{(c * 9/5 + 32):.2f} F")
elif targetUnit == "K":
    print(f"{(c + 273.15):.2f} K")
elif targetUnit == "R":
    print(f"{(c * 4/5):.2f} R")
::elab:endcode

::elab:begintest hint="-"
30 C
K
::elab:endtest

::elab:begintest hint="-"
80 F
C
::elab:endtest

::elab:begintest hint="-"
50 F
R
::elab:endtest

::elab:begintest hint="-"
90.7792 R
F
::elab:endtest

::elab:begintest hint="-"
-92.1536 F
F
::elab:endtest

::elab:begintest hint="-"
19.6544 F
F
::elab:endtest

::elab:begintest hint="-"
-90.1594 K
K
::elab:endtest

::elab:begintest hint="-"
39.6069 F
C
::elab:endtest

::elab:begintest hint="-"
4.0587 K
C
::elab:endtest

::elab:begintest hint="-"
25.1184 F
C
::elab:endtest

::elab:begintest hint="-"
48.0598 F
R
::elab:endtest

::elab:begintest hint="-"
-93.0373 R
C
::elab:endtest

::elab:begintest hint="-"
-95.5940 F
R
::elab:endtest