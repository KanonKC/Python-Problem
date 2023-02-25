# Unique Word Count

กำหนดให้ในแต่ละไฟล์จะมีบทความภาษาอังกฤษเขียนประมาณนี้

`paragraph1.txt`
<pre class="output">
There was nothing else to do. The deed had already been done and there was no going back. It now had been become a question of how they were going to be able to get out of this situation and escape.
</pre>

จงเขียนโปรแกรมที่รับชื่อไฟล์เข้าไป ตอบจำนวนคำทั้งหมด**ที่ไม่ซ้ำกัน**

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับชื่อไฟล์ที่ต้องการ

<u>ข้อมูลส่งออก</u>  
แสดงจำนวนคำทั้งหมดที่ไม่ซ้ำกันในไฟล์นั้น

**คำใบ้:** ลองศึกษาคำสั่ง `.strip()` และ `.lower()` สำหรับทำงานร่วมกับ String

## Example 1
<pre class="output">
File name: _paragraph1.txt_
Count: 32
</pre>

::elab:begincode blank=True
filename = input("File name: ")

records = []

with open(filename,'r') as f:
    data = f.readline().split()
    for word in data:
        if word.lower().strip('.') not in records:
            records.append(word.lower().strip('.'))
    print(f"Count: {len(records)}")
    print(records)
::elab:endcode

::elab:begintest hint="-"
paragraph1.txt
::elab:endtest
::elab:begintest hint="-"
paragraph2.txt
::elab:endtest
::elab:begintest hint="-"
paragraph3.txt
::elab:endtest
::elab:begintest hint="-"
paragraph4.txt
::elab:endtest
::elab:begintest hint="-"
paragraph5.txt
::elab:endtest