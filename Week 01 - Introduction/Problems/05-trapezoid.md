# Trapezoid

เขียนโปรแกรมที่หาค่าพื้นที่สี่เหลี่ยมคางหมู โดยรับความยาวของด้านคู่ขนาน 2 ด้านและความสูง (จากรูปก็คือ a,b และ h ตามลำดับ)

<img src="https://upload.wikimedia.org/wikipedia/commons/1/11/Trapezoid.svg">

<u>ข้อมูลนำเข้า</u>  
มี 3 บรรทัด แต่ละบรรทัดจะรับค่าเป็นจำนวนจริงบวก ด้านคู่ขนานด้านที่ 1, ด้านคู่ขนานด้านที่ 2, ความสูง ตามลำดับ  

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียวแสดงพื้นที่ของสี่เหลี่ยมคางหมูโดยแสดงเป็นทศนิยม 2 ตำแหน่ง  

<u>คำแนะนำ</u>  
ถ้าอยากให้โปรแกรมแสดงออกมาเป็นทศนิยม 2 ตำแหน่ง สามารถทำได้โดย `print(f"{number:.2f}")`  
**ตัวอย่าง 1** เรามีตัวแปร `number = 12.651432` หากเรา `print(f"{number:.2f}")` จะแสดงผลออกมาเป็น `12.65`  
**ตัวอย่าง 2** เรามีตัวแปร `number = 5` หากเรา `print(f"{number:.2f}")` จะแสดงผลออกมาเป็น `5.00`

## Example 1
<pre class="output">
a: _5.0_
b: _7_
h: _10_
60.00
</pre>

## Example 2
<pre class="output">
a: _7.65_
b: _6.25_
h: _10.00_
69.50
</pre>


::elab:begincode blank=True
a = float(input("a: "))
b = float(input("b: "))
h = float(input("h: "))

print(f"{1/2 * (a+b)*h:.2f}")
::elab:endcode

::elab:begintest hint="-"
4040.989
3122.372
2032.62
::elab:endtest
::elab:begintest hint="-"
5149
3455
3556.163
::elab:endtest
::elab:begintest hint="-"
4201.44
7480.697
4890.468
::elab:endtest
::elab:begintest hint="-"
6549.35
4469.591
3898.272
::elab:endtest
::elab:begintest hint="-"
8476.631
3549
1159
::elab:endtest
::elab:begintest hint="-"
268
4429.851
7198.546
::elab:endtest
::elab:begintest hint="-"
5126
9117
7150.599
::elab:endtest
::elab:begintest hint="-"
4995
3353.083
1698.968
::elab:endtest
::elab:begintest hint="-"
4621
4988.966
8091.378
::elab:endtest
::elab:begintest hint="-"
8223.28
5235
6776.425
::elab:endtest