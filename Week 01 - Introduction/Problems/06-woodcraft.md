# Woodcraft

โรงงานไม้แห่งหนึ่งสามารถผลิตสินค้าได้ 3 อย่างดังนี้:  

<style>
table,tr,td{
    border: 1px solid black;
    text-align: center;
}
</style>

<table>
<tr><td>สินค้า</td><td>กิ่งไม้ (Stick)</td><td>ไม้แผ่น (Slab)</td><td>ไม้ดิบ (Log)</td></tr>
<tr><td>เก้าอี้ (Chair)</td><td>4</td><td>1</td><td>0</td></tr>
<tr><td>โต๊ะ (Table)</td><td>6</td><td>3</td><td>1</td></tr>
<tr><td>ตู้เก็บของ (Storage)</td><td>2</td><td>2</td><td>4</td></tr>
</table>  

โดยจะเห็นว่าสินค้าแต่ละอย่างจะต้องใช้วัสดุในการก่อสร้างตามจำนวนที่กำหนด (กิ่งไม้/ไม้แผ่น/ไม้ดิบ)  

จงเขียนโปรแกรมที่จะรับค่าเป็นจำนวนของสินค้าแต่ละอย่าง และแสดงผลออกมาว่าจะต้องใช้วัสดุแต่ละชนิดอย่างละเท่าไหร่บ้าง

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 3 บรรทัด โดยแต่ละบรรทัดจะเป็นจำนวนเต็มโดยมีค่ามากกว่าเท่ากับ 0 โดยจำนวนของสินค้าที่ต้องการแต่ละชนิดคือเก้าอี้ โต๊ะ ตู้เก็บของ ตามลำดับ

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียวโดยแสดงจำนวนที่วัสดุแต่ละชนิดต้องใช้

## Example 1
<pre class="output">
Amount of Chair: _3_
Amount of Table: _1_
Amount of Storage: _2_
Stick x22
Slab x10
Log x9
</pre>

## Example 2
<pre class="output">
Amount of Chair: _5_
Amount of Table: _0_
Amount of Storage: _0_
Stick x20
Slab x5
Log x0
</pre>

::elab:begincode blank=True
chair = int(input("Amount of Chair: "))
table = int(input("Amount of Table: "))
storage = int(input("Amount of Storage: "))

stick = 4*chair + 6*table + 2*storage
slab  =   chair + 3*table + 2*storage
log   =           1*table + 4*storage

print(f"Stick x{stick}")
print(f"Slab x{slab}")
print(f"Log x{log}")
::elab:endcode

::elab:begintest hint="-"
2474
6773
531
::elab:endtest
::elab:begintest hint="-"
1713
3656
9278
::elab:endtest
::elab:begintest hint="-"
3611
3743
78
::elab:endtest
::elab:begintest hint="-"
502
539
3160
::elab:endtest
::elab:begintest hint="-"
5236
2718
6336
::elab:endtest
::elab:begintest hint="-"
8598
1973
1022
::elab:endtest
::elab:begintest hint="-"
4223
88
512
::elab:endtest
::elab:begintest hint="-"
6079
1350
4087
::elab:endtest
::elab:begintest hint="-"
7369
3237
601
::elab:endtest
::elab:begintest hint="-"
1163
5544
9202
::elab:endtest