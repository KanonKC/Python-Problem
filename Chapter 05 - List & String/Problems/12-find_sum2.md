# Find Sum 2

รับจำนวนเต็มเข้ามาหลายๆตัวภายในบรรทัดเดียว (โดยคั่นแต่ละตัวด้วย Spacebar) จากนั้นหาผลรวมของจำนวนทั้งหมดที่ใส่เข้ามา    
**คำใบ้:** [Split String](https://www.w3schools.com/python/ref_string_split.asp)

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็น "ข้อความจำนวนเต็ม" หลายตัว โดยแต่ละตัวจะคั่นด้วย Spacebar

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบเป็นผลรวมของจำนวนทั้งหมดที่ใส่เข้ามา

## Example 1
<pre class="output">
Enter integers: _1 2 3_
6
</pre>

## Example 2
<pre class="output">
Enter integers: _5_
5
</pre>

## Example 3
<pre class="output">
Enter integers: _1 -2 _ 
-1
</pre>

::elab:begincode blank=True
numbers = input("Enter integers: ").split()
numbers = [int(i) for i in numbers]

print(sum(numbers))
::elab:endcode

::elab:begintest hint="-"
1 2 3
::elab:endtest

::elab:begintest hint="-"
5
::elab:endtest

::elab:begintest hint="-"
1 -2
::elab:endtest

::elab:begintest hint="-"
0
::elab:endtest

::elab:begintest hint="-"
-1 -2 -3
::elab:endtest

::elab:begintest hint="-"
929389829 228 1284092 3878 19894 172
::elab:endtest

::elab:begintest hint="-"
-19 2839 28387 -2938298
::elab:endtest

::elab:begintest hint="-"
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
::elab:endtest