# Combination

เขียนโปรแกรมที่แสดงคำตอบจาก สูตรการจัดหมู่ดังรูป

\[nCr = \frac{n!}{r!(n-r)!}\]

**n** คือจำนวนของทั้งหมดที่เรามี  
**r** คือจำนวนของที่เราอยากเลือก (โดยที่ r ≤ n)  
**nCr** คือจำนวนวิธีทั้งหมดที่แตกต่างกัน ถ้าต้องเลือกของ r ชิ้น จากที่มีทั้งหมด n ชิ้น

สูตรข้างบนจะใช้หาว่าเมื่อเรามีของทั้งหมด n ชิ้น แล้วเราอยากเลือกของมาแค่ r ชิ้นจะทำได้กี่วิธี  

<u>ข้อมูลนำเข้า</u>  
บรรทัดที่ 1 รับเป็นจำนวนเต็มบวกหรือศูนย์ แทนจำนวนของทั้งหมดที่เรามี **n**    
บรรทัดที่ 2 รับเป็นจำนวนเต็มบวกหรือศูนย์ แทนจำนวนของที่เราอยากเลือก **r** โดยที่ r ≤ n

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์เป็นจำนวนวิธีการเลือกทั้งหมด เมื่อเลือกของ r ชิ้นจากที่มีทั้งหมด n ชิ้น

## Example 1
<pre class="output">
_5_
_3_
10
</pre>

## Example 2
<pre class="output">
_5_
_5_
1
</pre>

## Example 3
<pre class="output">
_5_
_0_
1
</pre>

::elab:begincode blank=True
def fac(n):
    if n == 0 or n == 1:
        return 1
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

n = int(input())
r = int(input())

print(fac(n)//(fac(r)*fac(n-r)))
::elab:endcode

::elab:begintest hint="-"
5
3
::elab:endtest
::elab:begintest hint="-"
10
10
::elab:endtest
::elab:begintest hint="-"
0
0
::elab:endtest
::elab:begintest hint="-"
6
0
::elab:endtest
::elab:begintest hint="-"
559
162
::elab:endtest
::elab:begintest hint="-"
488
49
::elab:endtest
::elab:begintest hint="-"
992
885
::elab:endtest
::elab:begintest hint="-"
806
16
::elab:endtest
::elab:begintest hint="-"
878
731
::elab:endtest
::elab:begintest hint="-"
940
464
::elab:endtest