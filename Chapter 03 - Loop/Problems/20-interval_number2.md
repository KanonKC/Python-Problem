# Interval Number 2

เขียนโปรแกรมที่รับจำนวนเต็มเข้ามา 2 ตัว จากนั้นแสดงตัวเลขทั้งหมดที่อยู่ระหว่างนั้น รวมถึงตัวเลข 2 ตัวที่รับเข้ามาด้วย  

โดยโจทย์ข้อนี้จะแตกต่างกับ `Interval Number` แบบแรกคือ สามารถนับเลขถอยหลังได้ หากตัวเลขตัวแรกที่รับเข้ามามีค่าน้อยกว่าตัวที่สอง

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นจำนวนเต็มทั้งคู่ `N1` และ `N2` ตามลำดับ

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
Start: _8_
End: _3_
8 7 6 5 4 3
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

if endNumber > startNumber:
    for i in range(startNumber,endNumber+1):
        print(i,end=" ")
else:
    for i in range(startNumber,endNumber-1,-1):
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
1401
81
::elab:endtest
::elab:begintest hint="-"
-50
645
::elab:endtest
::elab:begintest hint="-"
9188
-77
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
1083
90
::elab:endtest
::elab:begintest hint="-"
-45
-8251
::elab:endtest