# Pack of Number Sequence

รับจำนวนเต็มบวกเข้ามา 1 ตัว `N` โดยจะเป็นจำนวนคู่เท่านั้น จากนั้นเราจะแสดงลำดับตัวเลขที่แตกต่างกันทั้งหมด 6 แบบ โดยแต่ละแบบมีลักษณะ ดังนี้  

**ลำดับแบบที่ 1** - แสดงจำนวนเต็มบวกตั้งแต่ `0` ถึง `N`  
**ลำดับแบบที่ 2** - แสดงจำนวนเต็มบวกตั้งแต่ `N` ถึง `0`  
**ลำดับแบบที่ 3** - แสดงลำดับจำนวนคู่ตั้งแต่ `0` ทั้งหมด `N` ตัว  
**ลำดับแบบที่ 4** - แสดงลำดับคล้ายกับแบบที่ `1` แต่แสดงแค่ครึ่งหลังอย่างเดียว (อย่าลืมว่าจำนวน `N` จะเป็นแต่จำนวนคู่เท่านั้น ดังนั้นจะสามารถแบ่งคร่งได้พอดีอยู่แล้ว)  
**ลำดับแบบที่ 5** - แสดงลำดับกำลังสองตั้งแต่ `0` ทั้งหมด `N` ตัว  
**ลำดับแบบที่ 6** - แสดงลำดับจำนวนคี่ตั้งแต่ `0` ทั้งหมด `N` ตัว และมีค่าเป็นจำนวนเต็มบวก/ลบ สลับกันไป  

*แนะนำให้ดูตัวอย่างด้านล่าง จะเข้าใจมากข้น*

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มบวกคู่ `N`

<u>ข้อมูลส่งออก</u>  
แสดงลำดับตัวเลขที่แตกต่างกันทั้งหมด 6 แบบ ตามรายละเอียดข้างต้น

## Example 1
<pre class="output">
N: _5_
Sequence 1  
0 1 2 3 4 5 
Sequence 2  
5 4 3 2 1 0 
Sequence 3  
0 2 4 6 8   
Sequence 4  
2 3 4 5     
Sequence 5  
0 1 4 9 16  
Sequence 6  
1 -3 5 -7 9
</pre>

## Example 2
<pre class="output">
N: _10_
Sequence 1
0 1 2 3 4 5 6 7 8 9 10        
Sequence 2
10 9 8 7 6 5 4 3 2 1 0        
Sequence 3
0 2 4 6 8 10 12 14 16 18      
Sequence 4
5 6 7 8 9 10
Sequence 5
0 1 4 9 16 25 36 49 64 81     
Sequence 6
1 -3 5 -7 9 -11 13 -15 17 -19
</pre>

::elab:begincode blank=True
N = int(input("N: "))

print("Sequence 1")
for i in range(N+1):
    print(i,end=" ")

print()
print("Sequence 2")
for i in range(N,-1,-1):
    print(i,end=" ")

print()
print("Sequence 3")
for i in range(N):
    print(i*2,end=" ")

print()
print("Sequence 4")
for i in range(N//2,N+1):
    print(i,end=" ")

print()
print("Sequence 5")
for i in range(N):
    print(i**2,end=" ")

print()
print("Sequence 6")
for i in range(N):
    print((-1)**i*(2*i+1),end=" ")
::elab:endcode

::elab:begintest hint="-"
5
::elab:endtest

::elab:begintest hint="-"
10
::elab:endtest

::elab:begintest hint="-"
246
::elab:endtest
::elab:begintest hint="-"
729
::elab:endtest
::elab:begintest hint="-"
614
::elab:endtest
::elab:begintest hint="-"
975
::elab:endtest
::elab:begintest hint="-"
351
::elab:endtest
::elab:begintest hint="-"
647
::elab:endtest
::elab:begintest hint="-"
156
::elab:endtest
::elab:begintest hint="-"
555
::elab:endtest