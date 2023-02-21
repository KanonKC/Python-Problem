# Binary To Decimal

**เลขฐานสอง (ฺBinary)** หมายถึง ระบบเลขที่มีสัญลักษณ์เพียงสองตัวคือ 0 กับ 1

ตัวอย่างถ้าแปลงค่าเลขฐานสิบ มาเป็นเลขฐานสอง จะได้ดังนี้  

|Decimal|Binary|Decimal|Binary|
|-|-|-|-|
0 | `0000`|6 | `0110`
1 | `0001`|7 | `0111`
2 | `0010`|8 | `1000`
3 | `0011`|9 | `1001`
4 | `0100`|10| `1010`
5 | `0101`|

ให้เขียนโปรแกรมที่แปลงจากเลขฐาน 2 เป็นเลขฐาน 10

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับค่าเข้ามาเป็นตัวเลขฐาน 2 ที่ประกอบด้วย 0 หรือ 1 เท่านั้น

<u>ข้อมูลส่งออก</u>  
เลขฐาน 10 ของตัวเลขฐาน 2 ที่รับเข้ามา

## Example 1
<pre class="output">
Enter binary: __10__
2
</pre>

## Example 1
<pre class="output">
Enter binary: __111__
7
</pre>

## Example 1
<pre class="output">
Enter binary: __11101010111__
1879
</pre>

::elab:begincode blank=True
binary = input("Enter binary: ")

decimal = 0
for i in range(len(binary)):
    decimal += int(binary[-i-1]) * (2**i)

print(decimal)
::elab:endcode

::elab:begintest hint="-"
10
::elab:endtest
::elab:begintest hint="-"
111
::elab:endtest
::elab:begintest hint="-"
11101010111
::elab:endtest
::elab:begintest hint="-"
100101
::elab:endtest
::elab:begintest hint="-"
1010101001
::elab:endtest
::elab:begintest hint="-"
111011
::elab:endtest
::elab:begintest hint="-"
11010100100
::elab:endtest
::elab:begintest hint="-"
1000100100
::elab:endtest
::elab:begintest hint="-"
1010000100
::elab:endtest
::elab:begintest hint="-"
1111111111
::elab:endtest