# Interval Number

เขียนโปรแกรมที่รับจำนวนเต็มเข้ามา 2 ตัว จากนั้นแสดงตัวเลขทั้งหมดที่อยู่ระหว่างนั้น รวมถึงตัวเลข 2 ตัวที่รับเข้ามาด้วย

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นจำนวนเต็มทั้งคู่ `N1` และ `N2` ตามลำดับ โดยที่ `N1 ≤ N2`

<u>ข้อมูลส่งออก</u>  
แสดงจำนวนเต็มทั้งหมด ที่อยู่ระหว่าง `N1` และ `N2` รวมถึง 2 จำนวนนี้ด้วย

## Example 1
<pre class="output">
Start: _3_
End: _8_
3 4 5 6 7 8
</pre>

## Example 2
<pre class="output">
Start: _-5_
End: _5_
-5 -4 -3 -2 -1 0 1 2 3 4 5
</pre>

## Example 3
<pre class="output">
Start: _17_
End: _17_
17
</pre>

::elab:begincode blank=True
startNumber = int(input("Start: "))
endNumber = int(input("End: "))

for i in range(startNumber,endNumber+1):
    print(i,end=" ")
::elab:endcode

::elab:begintest hint="-"
3
8
::elab:endtest

::elab:begintest hint="-"
-5
5
::elab:endtest

::elab:begintest hint="-"
17
17
::elab:endtest

::elab:begintest hint="-"
81
1401
::elab:endtest
::elab:begintest hint="-"
-50
645
::elab:endtest
::elab:begintest hint="-"
-77
9188
::elab:endtest
::elab:begintest hint="-"
62
2477
::elab:endtest
::elab:begintest hint="-"
-47
2555
::elab:endtest
::elab:begintest hint="-"
90
1083
::elab:endtest
::elab:begintest hint="-"
-8251
-45
::elab:endtest