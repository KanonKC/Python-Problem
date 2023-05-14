# Only Positive

พัฒนาโปรแกรมรับจำนวนเต็มทีละค่า จนกระทั่งผู้ใช้พิมพ์เลข 0 หลังจากนั้น ให้แสดง **จำนวนครั้ง** ที่รับ *จำนวนเต็มบวก* เข้ามา

<u>ข้อมูลนำเข้า</u>  
มีหลายบรรทัด จนกว่าจะรับค่า `0` เป็นจำนวนเต็มบวกทั้งหมด  

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดงจำนวนครั้งที่รับจำนวนเต็มบวกเข้ามา

## Example 1
<pre class="output">
_1_
_2_
_-3_
_4_
0
Found 3 positive integer(s)
</pre>

## Example 2
<pre class="output">
_-1_
_-2_
_-3_
0
Found 0 positive integer(s)
</pre>

## Example 3
<pre class="output">
_0_
Found 0 positive integer(s)
</pre>

::elab:begincode blank=True
count = 0

while True:
    x = int(input())
    
    if x == 0:
        break
    elif x > 0:
        count += 1

print(f"Found {count} positive integer(s)")
::elab:endcode

::elab:begintest hint="-"
1
2
-3
4
0
::elab:endtest

::elab:begintest hint="-"
-1
-2
-3
0
::elab:endtest

::elab:begintest hint="-"
0
::elab:endtest

::elab:begintest hint="-"
-2052
-7561
9902
-1669
-7905
405
3585
4688
-3429
5208
9353
-968
8740
-8950
3687
-8881
9808
-2182
-6820
-965
0
::elab:endtest

::elab:begintest hint="-"
4185
-3211
-3460
-4816
-9659
1750
3993
-16
-7777
-5227
-5366
-5306
3677
9519
-3106
-2626
4153
-2634
3636
-6383
0
::elab:endtest

::elab:begintest hint="-"
-8829
-9244
-2633
-5977
-7790
-3573
-5175
-8447
-7617
-7437
-3130
-451
-5537
-6824
-6287
-1614
-9945
-9144
-7842
-8524
0
::elab:endtest

::elab:begintest hint="-"
1965
2295
-2618
7784
897
-7144
-8810
5797
-1433
-6720
3624
-4901
-7745
7831
1715
9451
-9604
-5484
-9599
5495
0
::elab:endtest

::elab:begintest hint="-"
6376
4767
2482
7464
-583
-4652
9142
3238
-7725
2925
4167
5004
4291
-9377
381
5824
5350
-1848
-9623
-5384
0
::elab:endtest

::elab:begintest hint="-"
1377
-7792
5272
-3629
5225
2359
-5019
1860
8145
-983
-8525
1662
6542
4824
2435
3036
-3742
8444
-3050
4961
0
::elab:endtest

::elab:begintest hint="-"
8470
2278
4247
7939
2853
2163
-5428
-3285
-239
9709
-2524
667
-3396
-2310
-6748
-5981
-4190
655
-7382
4633
0
::elab:endtest