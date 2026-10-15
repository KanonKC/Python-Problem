# Countdown

เขียนโปรแกรมที่รับจำนวนเต็มบวกเข้ามา 1 ตัว และนับเลขตั้งแต่ จำนวนนั้น จนถึง 0

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มบวก `N`

<u>ข้อมูลส่งออก</u>  
แสดงตัวเลขตั้งแต่ `N` จนถึง 0 โดยแสดงจำนวนละบรรทัด

::elab:begincode blank=True
n = int(input())

for i in range(n,-1,-1):
    print(i)
::elab:endcode

::elab:begintest hint="-"
3
::elab:endtest
::elab:begintest hint="-"
10
::elab:endtest
::elab:begintest hint="-"
2215
::elab:endtest
::elab:begintest hint="-"
5026
::elab:endtest
::elab:begintest hint="-"
7672
::elab:endtest
::elab:begintest hint="-"
9726
::elab:endtest
::elab:begintest hint="-"
6646
::elab:endtest
::elab:begintest hint="-"
7649
::elab:endtest
::elab:begintest hint="-"
1167
::elab:endtest
::elab:begintest hint="-"
7085
::elab:endtest