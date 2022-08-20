# Ribbon

เขียนโปรแกรมที่วาดรูปโบว์ โดยรับค่าเป็นขนาดของโบว์ ซึ่งขนาดจะเป็นแต่เลขคี่อย่างเดียวเท่านั้น 

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มคี่บวกแทนขนาดของโบว์

<u>ข้อมูลส่งออก</u>  
แสดงออกเป็นรูปโบว์ที่วาดโดยใช้ตัวอักษร `"#"`

## Example 1
<pre class="output">
_1_
\#
</pre>

## Example 2
<pre class="output">
_3_
\# #
\###
\# #
</pre>

## Example 3
<pre class="output">
_5_
\#   #
\## ##
\#####
\## ##
\#   #
</pre>

## Example 4
<pre class="output">
_7_
\#     #
\##   ##
\### ###
\#######
\### ###
\##   ##
\#     #
</pre>

::elab:begincode blank=True
n = int(input())

side = (n//2) + 1

for i in range(1,side):
    print(f"{'#'*i}{' '*(n-(2*i))}{'#'*i}")
print("#"*n)
for i in range(side-1,0,-1):
    print(f"{'#'*i}{' '*(n-(2*i))}{'#'*i}")
::elab:endcode

::elab:begintest hint="-"
1
::elab:endtest
::elab:begintest hint="-"
3
::elab:endtest
::elab:begintest hint="-"
5
::elab:endtest
::elab:begintest hint="-"
7
::elab:endtest
::elab:begintest hint="-"
91
::elab:endtest
::elab:begintest hint="-"
69
::elab:endtest
::elab:begintest hint="-"
74
::elab:endtest
::elab:begintest hint="-"
21
::elab:endtest
::elab:begintest hint="-"
42
::elab:endtest
::elab:begintest hint="-"
28
::elab:endtest