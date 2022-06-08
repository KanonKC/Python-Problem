# Introduce

เขียนโปรแกรมที่แนะนำตัวเอง โดยใส่ชื่อและปีเกิด(ค.ศ.) ของตัวเองเข้าไป ให้แสดงผลเป็นการแนะนำชื่อ และอายุของตนเอง *(ในการคำนวณอายุของโจทย์ข้อนี้ให้ยึดกว่าปีปัจจุบันเป็นปี ค.ศ. 2022 เสมอ)*

<u>ข้อมูลนำเข้า</u>  
บรรทัดที่ 1 รับข้อความเป็นชื่อ
บรรทัดที่ 2 รับจำนวนเต็มบวก เป็นปีเกิด(ค.ศ.) โดยปีเกิดจะน้อยกว่าปี 2022 เสมอ

<u>ข้อมูลส่งออก</u>  
แสดงข้อความแนะนำตัวเองออกมา ตามตัวอย่างด้านล่าง

## Example 1
<pre class="output">
Enter your name: _Tom_
Enter your age: _2005_
Hello, My name is Tom. I am 17 year(s) old.
</pre>

::elab:begincode blank=True
name = input("Enter your name: ")
birth = int(input("Enter your age: "))

print(f"Hello, My name is {name}. I am {2022-birth} year(s) old.")
::elab:endcode

::elab:begintest hint="-"
Tom
2005
::elab:endtest
::elab:begintest hint="-"
Jack
1984
::elab:endtest
::elab:begintest hint="-"
Bean
2012
::elab:endtest