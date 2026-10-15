# Reminder Theorem

เขียนโปรเเกรมรับค่า `p` แล้วหาเศษที่เหลือจากการหารสมการพหุนาม \(2x^4-5x^3-24x^2-7x+10\) ด้วย `x-p`

สามารถประยุกต์ใช้ความรู้เรื่องทฤษฎีบทเศษเหลือ [link](https://krupraiwan.wordpress.com/tag/ทฤษฎีบทเศษเหลือ) 

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็ม **p**

<u>ข้อมูลส่งออก</u>  
แสดงเศษที่เหลือจากการหารด้วยค่า p

::elab:begincode blank=True
x=int(input())
print("Fraction =",2*(x**4)-5*(x**3)-24*(x**2)-(7*x)+10)
::elab:endcode

::elab:begintest hint="test 1"
-1
::elab:endtest

::elab:begintest hint="test 2"
0
::elab:endtest

::elab:begintest hint="test 3"
1
::elab:endtest

::elab:begintest hint="test 4"
5
::elab:endtest

::elab:begintest hint="test 5"
2
::elab:endtest