# Multiple of 3 or 5

*(โจทย์ข้อนี้นำมาจากหนังสืิอ Python ๑๐๑ ภาควิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย)*  

เขียนโปรแกรมที่คำนวณหาผลรวมของจำนวนเต็มบวกทุกจำนวนที่มีค่า <u>ต่ำกว่า</u> จำนวนข้อมูลนำเข้า และที 3 หรือ 5 ที่เป็นตัวประกอบ เช่น หากข้อมูลนำเข้าคือ 20 คำตอบที่เราต้องการจะเท่ากับ <span style="color: red;">3+5+6+9+10+12+15+18 = 78</span> (คำตอบจะไม่ได้ผลรวม ที่รวมค่า 20 ไปด้วยเพราะต้องการค่าที่ต่ำกว่าอย่างเดียว)

**ข้อมูลนำเข้า**  
มีบรรทัดเดียว เป็นจำนวนเต็มบวก **n**

**ข้อมูลส่งออก**  
มีบรรทัดเดียว แสดงผลรวมของทุกจำนวนที่มีค่าน้อยกว่า **n** และมี 3 หรือ 5 เป็นตัวประกอบ

## Example 1
<pre class="output">
_20_
78
</pre>

## Example 2
<pre class="output">
_25_
143
</pre>

## Example 3
<pre class="output">
_3_
0
</pre>

::elab:begincode blank=True
n = int(input())
res = 0
for i in range(1,n):
    if i % 3 == 0 or i % 5 == 0:
        res += i    
print(res)
::elab:endcode

::elab:begintest hint="-"
20
::elab:endtest
::elab:begintest hint="-"
25
::elab:endtest
::elab:begintest hint="-"
3
::elab:endtest
::elab:begintest hint="-"
5
::elab:endtest
::elab:begintest hint="-"
15
::elab:endtest
::elab:begintest hint="-"
1205
::elab:endtest
::elab:begintest hint="-"
3333
::elab:endtest