# Text Wrap

เขียนโปรแกรมที่รับข้อความเข้ามา และจำนวนเต็ม 1 ตัว จากนั้นให้แสดงผลลัพธ์โดยที่ข้อความแต่ละแถวจะเหลือเท่ากับจำนวนที่ใส่ไป (ตัวที่ตัวอย่างด้านล่าง อาจจะเข้าใจมากกว่าก็ได้)

<u>ข้อมูลนำเข้า</u>  
บรรทัดที่ 1 รับเป็นข้อความ **s**  
บรรทัดที่ 2 รับเป็นจำนวนเต็มบวก **n** แทนจำนวนตัวอักษรที่มากที่สุดที่จะมีได้ใน 1 แถว

<u>ข้อมูลส่งออก</u>  
ข้อความ s ที่ถูกแบ่งบรรทัดตามจำนวน n

## Example 1
<pre class="output">
Input text: _ABCDEFGHIJKLIMNOQRSTUVWXYZ_
N: _4_
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
</pre>

## Example 2
<pre class="output">
Input text: _ABCDEFGHIJKLIMNOQRSTUVWXYZ_
N: _10_
ABCDEFGHIJ
KLIMNOQRST
UVWXYZ
</pre>

## Example 3
<pre class="output">
Input text: _ABCDEFGHIJKLIMNOQRSTUVWXYZ_
N: _26_
ABCDEFGHIJKLIMNOQRSTUVWXYZ
</pre>

::elab:begincode blank=True
s = input("Input text: ")
n = int(input("N: "))

for i in range(len(s)):
    if i % n == 0 and i != 0:
        print()
    print(s[i],end="")
::elab:endcode

::elab:begintest hint="-"
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
::elab:endtest
::elab:begintest hint="-"
ABCDEFGHIJKLIMNOQRSTUVWXYZ
10
::elab:endtest
::elab:begintest hint="-"
ABCDEFGHIJKLIMNOQRSTUVWXYZ
26
::elab:endtest
::elab:begintest hint="-"
ABCDEFGHIJKLIMNOQRSTUVWXYZABCDEFGHIJKLIMNOQRSTUVWXYZ
1
::elab:endtest
::elab:begintest hint="-"
ABCDEFGHIJKLIMNOQRSTUVWXYZABCDEFGHIJKLIMNOQRSTUVWXYZ
5
::elab:endtest
::elab:begintest hint="-"
ABCDEFGHIJKLIMNOQRSTUVWXYZABCDEFGHIJKLIMNOQRSTUVWXYZ
13
::elab:endtest
::elab:begintest hint="-"
ABCDEFGHIJKLIMNOQRSTUVWXYZABCDEFGHIJKLIMNOQRSTUVWXYZ
26
::elab:endtest
::elab:begintest hint="-"
ABCDEFGHIJKLIMNOQRSTUVWXYZABCDEFGHIJKLIMNOQRSTUVWXYZ
39
::elab:endtest