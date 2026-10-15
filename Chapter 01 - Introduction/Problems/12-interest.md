# Interest

เขียนโปรเเกรมเพื่อเเสดงเงินสุทธิที่ได้จากการฝากธนาคารแสดงเป็นทศนิยม 2 ตำแหน่ง ซึ่งสามารถคำนวณได้จากสูตรข้างล่างนี้  

<center>
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B300%7D%20A%20%3D%20P%28%5Cfrac%7B1&plus;r%7D%7Bn%7D%29%5E%7Bnt%7D" width="400">
</center>

เมื่อ P คือเงินตั้งต้น  
&nbsp;&nbsp;&nbsp;&nbsp;r คืออัตราดอกเบี้ย  
&nbsp;&nbsp;&nbsp;&nbsp;n คือจำนวนครั้งการจ่ายดอกเบี้ยทบต่อต่อปี  
&nbsp;&nbsp;&nbsp;&nbsp;t เป็นจำนวนปี

<u>ข้อมูลนำเข้า</u>  
รับค่า P, r, n และ t โดยเป็นจำนวนจริงบวกทั้งหมด

<u>ข้อมูลส่งออก</u>
แสดงเงินสุทธิ A

::elab:begincode blank=True
p=float(input())
r=float(input())
n=float(input())
t=float(input())
a=p*((1+r/n)**(n*t))
print(f'Final amount: {a:.2f}')
::elab:endcode

::elab:begintest hint="-"
10000
0.08
12
10
::elab:endtest

::elab:begintest hint="-"
50000
0.1
6
2
::elab:endtest

::elab:begintest hint="-"
100000
0.001
3
10
::elab:endtest

::elab:begintest hint="-"
1000
0.1
6
2
::elab:endtest

::elab:begintest hint="-"
9000
0.5
9
10
::elab:endtest