# List Comprehension: Alternating Sequence

สร้าง List ที่มีลักษณะตามตัวอย่างด้านล่าง  
<span style="color: red;">ลองใช้เทคนิคการสร้าง List แบบ List Comprehension เพื่อสามารถแก้ปัญหาโจทย์ข้อนี้ให้ได้  
**โดยเขียนโค้ดแค่ 1 บรรทัด**</span>

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มบวก  

<u>ข้อมูลส่งออก</u>  
แสดง List ที่มีลักษณะตามตัวอย่างด้านล่าง

## Example 1
<pre class="output">
N: _3_
[-1, 3, -5]
</pre>

## Example 2
<pre class="output">
N: _5_
[-1, 3, -5, 7, -9]
</pre>

## Example 3
<pre class="output">
N: _10_
[-1, 3, -5, 7, -9, 11, -13, 15, -17, 19]
</pre>

::elab:begincode blank=True
print([((i*2)-1)*((-1)**i) for i in range(1,int(input("N: "))+1)])
::elab:endcode

::elab:begintest hint="-"
3
::elab:endtest

::elab:begintest hint="-"
5
::elab:endtest

::elab:begintest hint="-"
10
::elab:endtest

::elab:begintest hint="-"
51
::elab:endtest

::elab:begintest hint="-"
1000
::elab:endtest

::elab:begintest hint="-"
1
::elab:endtest

