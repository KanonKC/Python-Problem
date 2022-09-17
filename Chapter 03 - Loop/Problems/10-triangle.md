# Triangle

***Recommend**: ก่อนจะลงมือจะทำโจทย์ข้อนี้ควรจะเคยทำ [rectangle](https://elabsheet.org/elab/taskpads/show/kps3c4mvtq/) มาก่อน*

เขียนโปรแกรมที่วาดรูปสามเหลี่ยมหน้าจั่ว โดยรับค่าเป็นความยาวข้างด้าน 2 ด้านที่เท่ากัน และบอกทิศทางของรูปสามเหลี่ยมหน้าจั่วว่าต้องการให้หันไปทางซ้ายหรือทางขวา

<u>ข้อมูลนำเข้า</u>  
**มีบรรทัดที่ 1** รับค่าเป็นจำนวนเต็มบวก แทนความยาวข้างด้าน 2 ด้านที่เท่ากัน  
**มีบรรทัดที่ 2** รับค่าเป็นข้อความเพื่อบอกทิศทางของรูปสามเหลี่ยมหน้าจั่วโดยถ้าใส่ `"left"` จะหันไปทางด้านซ้าย และ `"right"` จะเห็นไปทางด้านขวา (รับประกันว่าในการตรวจจะใส่แค่ 2 คำนี้เท่านั้น)

<u>ข้อมูลส่งออก</u>  
แสดงออกเป็นรูปสามเหลี่ยมหน้าจั่วที่วาดโดยใช้ตัวอักษร `#`

## Example 1
<pre class="output">
_5_
_right_
\#
\##
\###
\####
\#####
</pre>

## Example 2
<pre class="output">
_5_
_left_
    #
   ##
  ###
 ####
\#####
</pre>

## Example 3
<pre class="output">
_3_
_left_
  #
 ##
\###
</pre>

## Example 4
<pre class="output">
_1_
_left_
\#
</pre>

::elab:begincode blank=True
n = int(input())
side = input()

if side == 'left':
    for i in range(1,n+1):
        print(f"{' '*(n-i)}{'#'*i}")
else:
    for i in range(1,n+1):
        print('#'*i)
::elab:endcode

::elab:begintest hint="-"
69
left
::elab:endtest
::elab:begintest hint="-"
81
left
::elab:endtest
::elab:begintest hint="-"
2
left
::elab:endtest
::elab:begintest hint="-"
7
right
::elab:endtest
::elab:begintest hint="-"
59
right
::elab:endtest
::elab:begintest hint="-"
19
left
::elab:endtest
::elab:begintest hint="-"
24
left
::elab:endtest
::elab:begintest hint="-"
31
left
::elab:endtest
::elab:begintest hint="-"
64
left
::elab:endtest
::elab:begintest hint="-"
43
right
::elab:endtest