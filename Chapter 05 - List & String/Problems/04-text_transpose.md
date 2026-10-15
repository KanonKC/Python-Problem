# Text Transpose

***Recommend**: ก่อนจะลงมือจะทำโจทย์ข้อนี้ควรจะเคยทำ [text_wrap](https://elabsheet.org/elab/taskpads/show/evuu36hmx7/) มาก่อน*

เขียนโปรแกรมที่รับข้อความเข้ามา และจำนวนเต็ม 1 ตัว จากนั้นให้แสดงผลลัพธ์โดยข้อความจะถูกเขียนใหม่ เป็นแบบจากบนลงล่าง แล้วจึงซ้ายไปขวา โดยการเขียนจากบนลงล่างแต่ละครั้งจะมีจำนวนเท่ากับตัวเลขที่ใส่เข้ามา (ตัวที่ตัวอย่างด้านล่าง อาจจะเข้าใจมากกว่าก็ได้)

<u>ข้อมูลนำเข้า</u>  
บรรทัดที่ 1 รับเป็นข้อความ **s**  
บรรทัดที่ 2 รับเป็นจำนวนเต็มบวก **n** แทนจำนวนตัวอักษรที่มากที่สุดที่จะมีได้ใน 1 หลัก(Column)

<u>ข้อมูลส่งออก</u>  
ข้อความ s ที่ถูกเขียนจากบนลงล่าง ตามด้วยซ้ายไปขวา

::elab:begincode blank=True
text = input()
col = int(input())

result = ["" for i in range(col)]

for i in range(len(text)):
    result[i%col] += text[i]

for i in result:
    print(i)
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