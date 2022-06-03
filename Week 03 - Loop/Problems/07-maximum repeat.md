# Maximum Repeat

อ่านข้อมูลจากแป้นพิมพ์เป็นอักขระ 1 ตัวไปเรื่อยๆ จนกว่าจะพบคำว่า `"end"` จากนั้นให้ตอบว่าอักขระตัวใดที่มีการพิมพ์ติดซ้ำกันมากที่สุด พร้อมบอกจำนวนครั้งที่ติดกัน (ในการคำนวณให้ตัดค่า `"end"` ออกไป)

สำหรับรายละเอียดอื่นๆ ลองตัวในตัวอย่างจะเข้าใจง่ายกว่า

**ข้อมูลนำเข้า**  
รับค่าเป็นข้อความ สามารถรับค่าได้เรื่อยๆ (มีข้อความใส่เข้ามาได้หลายบรรทัด) จนกว่าจะเจอค่า `"end"`

**ข้อมูลส่งออก**  
มีบรรทัดเดียว แสดงอักขระที่พิมพ์ติดซ้ำกันมากที่สุด (ในการคำนวณให้ตัดค่า `"end"` ออกไป) และ จำนวนครั้งที่ติดกัน

## Example 1
<pre class="output">
_A_
_A_
_A_
_A_
_A_
_B_
_C_
_end_
Most Repeat: 'A' at 5 Count(s)
</pre>
**คำอธิบาย:** คำตอบจะไฮไลท์ด้วยสีแดง <span style="color: red;">A A A A A</span> B C


## Example 2
<pre class="output">
_A_
_A_
_B_
_B_
_B_
_C_
_C_
_end_
Most Repeat: 'B' at 3 Count(s)
</pre>

**คำอธิบาย:** คำตอบจะไฮไลท์ด้วยสีแดง A A <span style="color: red;">B B B</span> C C


## Example 3
<pre class="output">
_A_
_A_
_B_
_B_
_C_
_C_
_end_
Most Repeat: 'A' at 2 Count(s)
</pre>

**คำอธิบาย:** คำตอบจะไฮไลท์ด้วยสีแดง  <span style="color: red;">A A</span> B B C C จะเห็นว่าในตัวอย่างนี้ทั้ง A,B,C ต่างซ้ำอย่างเท่ากัน ให้จำไว้ว่าเราจะไม่เปลี่ยนคำตอบจนกว่าจะเจอตัวที่**มากกว่าเท่านั้น**


## Example 4
<pre class="output">
_X_
_X_
_Y_
_Y_
_Y_
_Z_
_Z_
_Z_
_Z_
_Y_
_Y_
_end_
Most Repeat: 'Z' at 4 Count(s)
</pre>
**คำอธิบาย:** คำตอบจะไฮไลท์ด้วยสีแดง X X Y Y Y <span style="color: red;">Z Z Z Z</span> Y  Y แม้ว่า Y จะมีจำนวนรวมมากว่า Z ก็จริง แต่เราสนใจแค่ติดกันมากที่สุด ดังนั้นการติดกันของ Z 4 ครั้งเลยเป็นคำตอบ

::elab:begincode blank=True
max_char = ""
max_count = 0

current_char = ""
current_count = 0

while True:
    x = input("")
    if x == "end":
        if current_count > max_count:
            max_count = current_count
            max_char = current_char
        break
    if x == current_char:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
            max_char = current_char
        current_char = x
        current_count = 1


print(f"Most Repeat: '{max_char}' at {max_count} Count(s)")
::elab:endcode

::elab:begintest hint="-"
A
A
A
A
A
B
C
end
::elab:endtest
::elab:begintest hint="-"
A
A
B
B
B
C
C
end
::elab:endtest
::elab:begintest hint="-"
A
A
B
B
C
C
end
::elab:endtest
::elab:begintest hint="-"
X
X
Y
Y
Y
Z
Z
Z
Z
Y
Y
end
::elab:endtest
::elab:begintest hint="-"
K
K
K
K
K
end
::elab:endtest
::elab:begintest hint="-"
2
5
5
5
5
3
5
8
5
5
end
::elab:endtest
::elab:begintest hint="-"
2
7
7
7
2
2
1
2
2
2
end
::elab:endtest