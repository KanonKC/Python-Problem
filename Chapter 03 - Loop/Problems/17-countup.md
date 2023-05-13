# Countup

เขียนโปรแกรมที่รับจำนวนเต็มบวกเข้ามา 1 ตัว และนับเลขตั้งแต่ 0 จนถึงจำนวนนั้น

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มบวก `N`

<u>ข้อมูลส่งออก</u>  
แสดงตัวเลขตั้งแต่ 0 จนถึง `N` โดยแสดงจำนวนละบรรทัด

## Example 1
<pre class="output">
Countup to: _3_
0
1
2
3
</pre>

## Example 2
<pre class="output">
Countup to: _10_
0
1
2
3
4
5
6
7
8
9
10
</pre>

::elab:begincode blank=True
n = int(input("Countup to: "))

for i in range(n+1):
    print(i)
::elab:endcode

::elab:begintest hint="-"
3
::elab:endtest
::elab:begintest hint="-"
10
::elab:endtest
::elab:begintest hint="-"
2215
::elab:endtest
::elab:begintest hint="-"
5026
::elab:endtest
::elab:begintest hint="-"
7672
::elab:endtest
::elab:begintest hint="-"
9726
::elab:endtest
::elab:begintest hint="-"
6646
::elab:endtest
::elab:begintest hint="-"
7649
::elab:endtest
::elab:begintest hint="-"
1167
::elab:endtest
::elab:begintest hint="-"
7085
::elab:endtest