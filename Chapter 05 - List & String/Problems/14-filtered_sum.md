# Filtered Sum

รับจำนวนเข้ามาหลายๆตัวภายในบรรทัดเดียว (โดยคั่นแต่ละตัวด้วย Spacebar) จากนั้นหาผลรวมทั้งหมด **โดยที่จะไม่นำจำนวนทศนิยมที่ใส่เข้ามา คิดด้วย**  

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็น "ข้อความจำนวน" หลายตัว โดยแต่ละตัวจะคั่นด้วย Spacebar

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบเป็นผลรวมของจำนวนทั้งหมดที่ใส่เข้ามา โดยไม่นำจำนวนทศนิยมมารวม

## Example 1
<pre class="output">
Enter integers: _1 2 3_
6
</pre>

## Example 2
<pre class="output">
Enter integers: _1 0.23 0.239 2 0.30 3 0.99 0.1_
6
</pre>

## Example 3
<pre class="output">
Enter integers: _5.0_
0
</pre>

::elab:begincode blank=True
numbers = input("Enter integers: ").split()
numbers = [int(i) for i in numbers if '.' not in i]

print(sum(numbers))
::elab:endcode

::elab:begintest hint="-"
1 2 3
::elab:endtest

::elab:begintest hint="-"
1 0.23 0.239 2 0.30 3 0.99 0.1
::elab:endtest

::elab:begintest hint="-"
5.0
::elab:endtest

::elab:begintest hint="-"
0
::elab:endtest

::elab:begintest hint="-"
-1 -0.27 -2 -3
::elab:endtest

::elab:begintest hint="-"
929389829 228.23 1284092 3878.20 19894 172 0.2938
::elab:endtest

::elab:begintest hint="-"
-19 2839 28387 -2938298
::elab:endtest

::elab:begintest hint="-"
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
::elab:endtest

::elab:begintest hint="-"
0.23 0.35835 0.384 0.348 0.123
::elab:endtest