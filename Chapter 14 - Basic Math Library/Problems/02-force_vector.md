# Vector of Force

รับขนาดของแรง และมุมที่แรงมีต่อแกน x จากนั้นแตกเป็น แรงที่แรงมีต่อแกน x และแกน y   

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1** เป็นจำนวนจริงแทนขนาดของแรง (F)  
**บรรทัดที่ 2** เป็นจำนวนจริงแทนมุมที่แรงมีต่อแกน x เป็นหน่วยองศา  

<u>ข้อมูลส่งออก</u>  
**บรรทัดที่ 1** แทนขนาดของแรงในแกน x แสดงเป็นทศนิยม 2 ตำแหน่ง  
**บรรทัดที่ 2** แทนขนาดของแรงในแกน y แสดงเป็นทศนิยม 2 ตำแหน่ง  

## Example 1
<pre class="output">
Enter force: _10_
Enter angle: _53_
Horizontal component: 6.02
Vertical component: 7.99
</pre>

## Example 2
<pre class="output">
Enter force: _15_
Enter angle: _90_
Horizontal component: 0.00
Vertical component: 15.00
</pre>

::elab:begincode blank=True
from math import sin, cos, radians

f = float(input("Enter force: "))
a = float(input("Enter angle: "))

print(f"Horizontal component: {f*cos(radians(a)):.2f}")
print(f"Vertical component: {f*sin(radians(a)):.2f}")
::elab:endcode

::elab:begintest hint="-"
10
53

::elab:endtest
::elab:begintest hint="-"
15
90

::elab:endtest
::elab:begintest hint="-"
15
0

::elab:endtest
::elab:begintest hint="-"
123
17

::elab:endtest