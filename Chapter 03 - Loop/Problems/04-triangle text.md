# Triangle Text

เขียนโปรแกรมที่จะรับข้อความ และความสูงของสามเหลี่ยมให้ แสดงผลลัพธ์ออกมาเหมือนกับตัวอย่างด้านล่าง โดยแต่ละบรรทัดจะมีจำนวนช่อง Spacebar เพิ่มขึ้นทีละ 1

<u>ข้อมูลนำเข้า</u>  
บรรทัดที่ 1 รับเป็นข้อความที่จะแสดงผล  
บรรทัดที่ 2 รับตัวเลขเป็นจำนวนเต็มแทนความสูงของสามเหลี่ยม

<u>ข้อมูลส่งออก</u>  
แสดงข้อความออกมาโดยมีจำนวนบรรทัดเท่ากับความสูง และในแต่ละชั้นจะมีอักขระว่าง(Spacebar) เพิ่มขึ้นที่ละ 1

::elab:begincode blank=True
text = input()
h = int(input())

for i in range(h):
    print(f"{' '*i}{text}")
::elab:endcode

::elab:begintest hint="-"
asdfghjkl
10
::elab:endtest
::elab:begintest hint="-"
kheeojg
7
::elab:endtest
::elab:begintest hint="-"
aaaaaaaaaaaa
5
::elab:endtest
::elab:begintest hint="-"
oiuhnmkij
20
::elab:endtest
::elab:begintest hint="-"
z
99
::elab:endtest