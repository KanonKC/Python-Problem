# Rounding Number

เขียนโปรแกรมที่รับตัวเลขค่านึงเข้ามา จากนั้นให้ปัดเลขนั้นให้เหลือตำแหน่งทศนิยมตามที่เราต้องการ

<u>ข้อมูลนำเข้า</u>  
**มีบรรทัดที่ 1** เป็นตัวเลขทศนิยม  
**มีบรรทัดที่ 2** เป็นจำนวนเต็มบวก แทนตำแหน่งทศนิยมที่เราต้องการหลังจากปัดค่าแล้ว

<u>ข้อมูลส่งออก</u>  
ตัวเลขทศนิยมที่ปัดค่าตามที่ต้องการแล้ว

::elab:begincode blank=True
value = input()
precision = int(input()) + 1

pre_position = value.index('.') + precision

target = int(value[pre_position])
next = int(value[pre_position - 1])
result = value[:pre_position - 1]

if target <= 4 or (target == 5 and next % 2 == 0):
    result += str(next)
elif target >= 6 or (target == 5 and next % 2 != 0):
    result += str(next+1)

print(result)
::elab:endcode

::elab:begintest hint="-"
1.62712
3
::elab:endtest
::elab:begintest hint="-"
1.62712
2
::elab:endtest
::elab:begintest hint="-"
1.65
1
::elab:endtest
::elab:begintest hint="-"
1.35
1
::elab:endtest
::elab:begintest hint="-"
0.17454008
4
::elab:endtest
::elab:begintest hint="-"
1.6725419
5
::elab:endtest
::elab:begintest hint="-"
0.9398962
2
::elab:endtest
::elab:begintest hint="-"
1.2917862782
1
::elab:endtest
::elab:begintest hint="-"
0.27778622
3
::elab:endtest
::elab:begintest hint="-"
1.8534532
1
::elab:endtest