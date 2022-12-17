# Even Odd

เขียนโปรแกรมที่รับตัวเลขจำนวนเต็มเข้ามา และตอบว่าเป็นจำนวนคู่ (Even) หรือจำนวนคี่ (Odd) 

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็นจำนวนเต็มบวก **n**

<u>ข้อมูลส่งออก</u>  
คำว่า Hello World!

## Example 1
<pre class="output">
_2_
Even
</pre>

## Example 2
<pre class="output">
_3_
Odd
</pre>

## Example 3
<pre class="output">
_2637_
Odd
</pre>

::elab:begincode blank=True
n = int(input())

if n % 2 == 0:
    print("Even")
else:
    print("Odd")
::elab:endcode

::elab:begintest hint="-"
2
::elab:endtest
::elab:begintest hint="-"
3
::elab:endtest
::elab:begintest hint="-"
2637
::elab:endtest
::elab:begintest hint="-"
381360
::elab:endtest
::elab:begintest hint="-"
241064
::elab:endtest
::elab:begintest hint="-"
639149
::elab:endtest
::elab:begintest hint="-"
82899
::elab:endtest
::elab:begintest hint="-"
318205
::elab:endtest
::elab:begintest hint="-"
608696
::elab:endtest
::elab:begintest hint="-"
946298
::elab:endtest