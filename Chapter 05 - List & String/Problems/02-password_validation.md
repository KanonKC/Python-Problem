# Password Validation

ในการตั้งรหัสผ่านมักจะมีเงื่อนไขต่างๆขึ้นมาให้เราทำตาม เพื่อให้รหัสผ่านของเรามีความแข็งแรง และไม่ให้ใครมาไขรหัสผ่านเราได้  

โดยปกติแล้วการตั้งรหัสผ่านมักจะมีเงื่อนไขดังนี้:

- The password length must be greater than or equal to 8 (ต้องมีความยาวอย่างน้อย 8 ตัวอักษร)
- The password must contain one or more uppercase characters (ต้องมีอักขระตัวพิมพ์ใหญ่ A-Z)
- The password must contain one or more lowercase characters (ต้องมีอักขระตัวพิมพ์เล็ก a-z)
- The password must contain one or more numeric values (ต้องมีตัวเลข 0-9)
- The password must contain one or more special characters (ต้องมีตัวอักษรพิเศษเช่น !, @, #, $, %, ^, &, *)

เขียนโปรแกรมที่รับรหัสผ่านมา จากนั้นตรวจสอบว่ารหัสผ่านนั้นตรงตามเงื่อนไขทั้ง 5 อย่างที่เขียนไว้ข้างบนหรือไม่ หากไม่ตรงกับเงื่อนไขไหนให้แสดงข้อความภาษาอังกฤษเหมือนกับด้านบน แต่หากรหัสผ่านที่รับมาถูกต้องตามเงื่อนไขทั้งหมดให้แสดงข้อความว่า `Your password is strong!`


<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับข้อความเป็นรหัสผ่านที่ต้องการตรวจสอบ

<u>ข้อมูลส่งออก</u>  
แสดงข้อความที่บอกว่ารหัสผ่านขาดเงื่อนอะไร หรือครบเงื่อนไขแล้ว

## Example 1
<pre class="output">
Enter a password: _1q2w3e4r_
The password must contain one or more uppercase characters
The password must contain one or more special characters
</pre>

## Example 2
<pre class="output">
Enter a password: _!Q@W#E$R_
The password must contain one or more lowercase characters
The password must contain one or more numeric values
</pre>

## Example 3
<pre class="output">
Enter a password: _@_
The password length must be greater than or equal to 8
The password must contain one or more uppercase characters
The password must contain one or more lowercase characters
The password must contain one or more numeric values
</pre>

## Example 4
<pre class="output">
Enter a password: _ask29BS&^n8a^S8b_
Your password is strong!
</pre>

::elab:begincode blank=True
password = input("Enter a password: ")

length = len(password) >= 8
upper = False
lower = False
number = False
special = False

for i in password:
    if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
        upper = True
    elif i in "qwertyuiopasdfghjklzxcvbnm":
        lower = True
    elif i in "0123456789":
        number = True
    elif i in "!@#$%^&*":
        special = True

if not length:
    print("The password length must be greater than or equal to 8")
if not upper:
    print("The password must contain one or more uppercase characters")
if not lower:
    print("The password must contain one or more lowercase characters")
if not number:
    print("The password must contain one or more numeric values")
if not special:
    print("The password must contain one or more special characters")

if length and upper and lower and number and special:
    print("Your password is strong!")
::elab:endcode

::elab:begintest hint="-"
1q2w3e4r
::elab:endtest
::elab:begintest hint="-"
AC#@
::elab:endtest
::elab:begintest hint="-"
aksjk*&*287187JskL
::elab:endtest
::elab:begintest hint="-"
skldklskdlkslkdlksldkl
::elab:endtest
::elab:begintest hint="-"
a
::elab:endtest
::elab:begintest hint="-"
1
::elab:endtest