# Duo Eater

ปั้นกับเกนมักจะออกไปหาอะไรกินด้วยกันเสมอซึ่งการกินในแต่ละครั้งของทั้งคู่จะมีรูปแบบดังนี้  
&nbsp;&nbsp;&nbsp;&nbsp;เมื่อได้รับอาหารมา S ส่วน ปั้นจะกินครั้งละ P ส่วน และจะกินไปเรื่อย ๆ จนกระทั่งเหลืออาหารไม่ถึง P ส่วน จากนั้นจะยกให้เกนกิน เกนจะกินครั้งละ G ส่วน และจะกินไปเรื่อย ๆ จนกระทั่งเหลืออาหารไม่ถึง G ส่วน ซึ่งจะนำอาหารที่เหลือนี้ไปให้สุนัขกิน  
จงเขียนโปรแกรมที่รับค่า S P และ G และแสดงผลว่าปั้นกินไปกี่ครั้ง เกนกินไปกี่ครั้ง และ เหลือหารหารให้สุนัขกี่ส่วน  

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 3 บรรทัด เป็นจำนวนเต็มบวกทั้งหมด  
**บรรทัดที่ 1** แทนจำนวนอาหารทั้งหมด ในตอนแรก  
**บรรทัดที่ 2** แทนจำนวนอาหารที่ปั้นจะกิน ในแต่ละครั้ง  
**บรรทัดที่ 3** แทนจำนวนอาหารที่เกนจะกิน ในแต่ละครั้ง  

<u>ข้อมูลส่งออก</u>  
มีทั้งหมด 3 บรรทัด  
**บรรทัดที่ 1** แสดงจำนวนอาหารที่ปั้นกินไปทั้งหมด  
**บรรทัดที่ 2** แสดงจำนวนอาหารที่เกนกินไปทั้งหมด  
**บรรทัดที่ 3** แสดงจำนวนอาหารที่เหลือ

## Example
<pre class="output">
Input starting food (S): _197_
Input Paun's eating rate (P): _70_
Input Gane's eating rate (n): _11_
Paun eats 2 time(s)
Gane eats 5 time(s)
Remaining 2 for dog
</pre>

::elab:begincode blank=True
s=int(input("Input starting food (S): "))
p=int(input("Input Paun's eating rate (P): "))
n=int(input("Input Gane's eating rate (n): "))
pe=s//p
ge=(s-(p*pe))//n
dog=s-(p*pe)-(ge*n)
print(f"Paun eats {pe} time(s)")
print(f"Gane eats {ge} time(s)")
print(f"Remaining {dog} for dog")
::elab:endcode

::elab:begintest hint="test 1"
197
70
11
::elab:endtest

::elab:begintest hint="test 2"
100
50
25
::elab:endtest

::elab:begintest hint="test 3"
200
7
2
::elab:endtest

::elab:begintest hint="test 4"
99
2
1
::elab:endtest

::elab:begintest hint="test 5"
1000
7
5
::elab:endtest