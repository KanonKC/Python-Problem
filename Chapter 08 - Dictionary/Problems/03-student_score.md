# Student Score

รับชื่อของนักเรียนแต่ละคน และคะแนนของนักเรียนแต่ละคน จากนั้นแสดงคะแนนเฉลี่ยนและชื่อของนักเรียนที่ได้คะแนนสมากกว่าค่าเฉลี่ย

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1** รับจำนวนเต็ม `N` เข้ามา ซึ่งเป็นจำนวนนักเรียนทั้งหมดที่เราจะรับ  
**จากนั้นอีก N บรรทัด** รับเป็นข้อความที่เป็นชื่อของนักเรียน และคะแนนที่ได้ (คั่นด้วย Spacebar)  

<u>ข้อมูลส่งออก</u>  
แสดงคะแนนเฉลี่ย  
จากนั้นแต่ละบรรทัดแสดงรายชื่อของนักเรียนที่ได้คะแนนสูงกว่าค่าเฉลี่ยนั้น

## Example 1
<pre class="output">
Number of students: _5_
_Alice 85_
_Bob 90_
_Charlie 78_
_David 92_
_Eve 88_
Average score: 86.60
Students with score above or equal to average:
Bob
David
Eve
</pre>

::elab:begincode blank=True
N = int(input("Number of students: "))

students = {}
totalScore = 0
for i in range(N):
    x = input().split()
    name = x[0]
    score = float(x[1])
    
    totalScore += score
    students[name] = score

averageScore = totalScore / N

print(f"Average score: {averageScore:.2f}")
print("Students with score above or equal to average:")
for name in students:
    if students[name] >= averageScore:
        print(name)
::elab:endcode

::elab:begintest hint="-"
5
Alice 85
Bob 90
Charlie 78
David 92
Eve 88
::elab:endtest

::elab:begintest hint="-"
5
Alice 75
Bob 75
Charlie 75
David 75
Eve 75
::elab:endtest

::elab:begintest hint="-"
7
Alice 85
Bob 90
Charlie 78
David 92
Eve 88
Fiona 95
Grace 89
::elab:endtest

::elab:begintest hint="-"
5
Alice 92
Bob 80
Charlie 65
David 88
Eve 78
::elab:endtest

::elab:begintest hint="-"
5
Alice 65
Bob 80
Charlie 95
David 70
Eve 85
::elab:endtest