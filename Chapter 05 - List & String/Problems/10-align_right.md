# Align Right

เขียนโปรแกรมที่รับข้อความเข้ามาเรื่อยๆ ทีละบรรทัดจนกว่าจะกด Enter โดยไม่พิมพ์อะไร จากนั้นให้แสดงข้อความทั้งหมดใหม่ทีละบรรทัด โดยทุกข้อความจะชิดขวาแทน



<u>ข้อมูลนำเข้า</u>  
มีหลายบรรทัด แต่ละบรรทัดรับข้อความเข้ามา  
สามารถรับข้อความได้เรื่อยๆ จนกว่าจะรับข้อความเปล่ามา

<u>ข้อมูลส่งออก</u>  
แสดงข้อความทั้งหมด แบบชิดขวา

## Example 1
<pre class="output">
_Hello_
_Welcome_
_To_
_Init_
_Me_
_↵_
  Hello
Welcome
     To
   Init
     Me
</pre>
↵ หมายถึงกด Enter ไปเลย โดยไม่ใส่อะไร

## Example 2
<pre class="output">
_1_
_22_
_333_
_↵_
  1
 22
333
</pre>

::elab:begincode blank=True
words = []
max_len = 0

while True:
    text = input()

    if text == "":
        break

    words.append(text)
    max_len = max(max_len,len(text))

for word in words:
    print(f"{' '*(max_len-len(word))}{word}")
::elab:endcode

::elab:begintest hint="-"
Hello
Welcome
To
Init
Me

::elab:endtest
::elab:begintest hint="-"
1
22
333

::elab:endtest
::elab:begintest hint="-"
kslkdklsk
sldklksldklskdllskdl
sldk
sldkkd
sld
s
dklskdl

::elab:endtest
::elab:begintest hint="-"
a
a
a
a
a

::elab:endtest