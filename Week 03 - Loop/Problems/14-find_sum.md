# Find Sum

รับจำนวนเต็มเข้ามาเรื่อยๆ จนกว่าจะพบเลข 0 จากนั้นให้หาผมรวมของจำนวนทั้งหมดที่ใส่เข้ามา

<u>ข้อมูลนำเข้า</u>  
รับค่าเป็นจำนวนเต็มบวก สามารถรับค่าได้เรื่อยๆ (มีจำนวนจริงใส่เข้ามาได้หลายบรรทัด) จนกว่าจะเจอค่า 0

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบเป็นผลรวมของจำนวนทั้งหมดที่ใส่เข้ามา

## Example 1
<pre class="output">
_1_
_2_
_3_
_0_
6
</pre>

## Example 2
<pre class="output">
_5_
_5_
_5_
_0_
15
</pre>

## Example 3
<pre class="output">
_0_
0
</pre>

::elab:begincode blank=True
total = 0
while True:
    x = int(input())
    if x == 0:
        break
    total += x
print(total)
::elab:endcode

::elab:begintest hint="-"
290549
957523
206624
0
::elab:endtest
::elab:begintest hint="-"
61369
631195
584700
753166
605471
907098
805981
807423
146020
0
::elab:endtest
::elab:begintest hint="-"
76755
206437
752470
618304
496738
687924
452532
713397
0
::elab:endtest
::elab:begintest hint="-"
427837
554043
878965
620126
339557
777436
62127
102656
111230
0
::elab:endtest
::elab:begintest hint="-"
629734
422158
520676
341078
22879
437452
476885
50118
0
::elab:endtest
::elab:begintest hint="-"
719007
326254
363817
525749
964093
639752
833919
586184
442130
11873
0
::elab:endtest
::elab:begintest hint="-"
558408
184670
575860
418824
526220
206526
564847
418279
0
::elab:endtest
::elab:begintest hint="-"
243782
66339
422166
0
::elab:endtest
::elab:begintest hint="-"
492370
485360
424613
199470
322897
575638
0
::elab:endtest
::elab:begintest hint="-"
0
::elab:endtest