# List Comprehension: Capital Only

สร้าง List ที่มีลักษณะตามตัวอย่างด้านล่าง  
<span style="color: red;">ลองใช้เทคนิคการสร้าง List แบบ List Comprehension เพื่อสามารถแก้ปัญหาโจทย์ข้อนี้ให้ได้  
**โดยเขียนโค้ดแค่ 1 บรรทัด**</span>

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มบวก  

<u>ข้อมูลส่งออก</u>  
แสดง List ที่มีลักษณะตามตัวอย่างด้านล่าง

## Example 1
<pre class="output">
Enter words: _Hello My Name Is John_
['H', 'M', 'N', 'I', 'J']
</pre>

## Example 2
<pre class="output">
Enter words: _Welcome To My House_
['W', 'T', 'M', 'H']
</pre>

::elab:begincode blank=True
print([i[0] for i in input("Enter words: ").split()])::elab:endcode

::elab:begintest hint="-"
Hello My Name Is John
::elab:endtest

::elab:begintest hint="-"
Welcome To My House
::elab:endtest

::elab:begintest hint="-"
asd wad wd wd wa sd wa dsd w ds a a a
::elab:endtest