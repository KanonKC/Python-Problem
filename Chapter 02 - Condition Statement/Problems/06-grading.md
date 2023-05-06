# Grading

*(โจทย์ข้อนี้นำมาจากหนังสืิอ Python ๑๐๑ ภาควิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย)*  

ในการตัดเกรดวิชามีลักษณะเป็นไปตามตารางดังนี้

<style>
table,tr,td{
    border: 1px solid black;
    text-align: center;
}
</style>

<table>
<tr><td>คะแนนรวม (x)</td><td>เกรด</td></tr>
<tr><td>80 ≤ x ≤ 100 </td><td>A</td></tr>
<tr><td>75 ≤ x < 80  </td><td>B+</td></tr>
<tr><td>70 ≤ x < 75  </td><td>B</td></tr>
<tr><td>65 ≤ x < 70  </td><td>C+</td></tr>
<tr><td>60 ≤ x < 65  </td><td>C</td></tr>
<tr><td>55 ≤ x < 60  </td><td>D+</td></tr>
<tr><td>50 ≤ x < 55  </td><td>D</td></tr>
<tr><td>0  ≤ x < 50  </td><td>F</td></tr>
</table>  

ให้เขียนโปรแกรมที่รับคะแนนทั้งหมด และแสดงออกมาว่าจะได้เกรดอะไร

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว แทนคะแนนทั้งหมด เป็นจำนวนจริง **x** โดยที่ 0 <= x <= 100

<u>ข้อมูลส่งออก</u>  
แสดงเกรดที่จะได้รับ

## Example 1
<pre class="output">
_87_
A
</pre>

## Example 2
<pre class="output">
_69.95_
C+
</pre>

## Example 3
<pre class="output">
_40_
F
</pre>

::elab:begincode blank=True
x = float(input())

if x >= 80:
    print("A")
elif x >= 75:
    print("B+")
elif x >= 70:
    print("B")
elif x >= 65:
    print("C+")
elif x >= 60:
    print("C")
elif x >= 55:
    print("D+")
elif x >= 50:
    print("D")
else:
    print("F")

::elab:endcode

::elab:begintest hint="-"
83.199
::elab:endtest
::elab:begintest hint="-"
51.65
::elab:endtest
::elab:begintest hint="-"
61.078
::elab:endtest
::elab:begintest hint="-"
77.889
::elab:endtest
::elab:begintest hint="-"
40.145
::elab:endtest
::elab:begintest hint="-"
58.32
::elab:endtest
::elab:begintest hint="-"
100
::elab:endtest
::elab:begintest hint="-"
93.381
::elab:endtest
::elab:begintest hint="-"
67.094
::elab:endtest
::elab:begintest hint="-"
70.158
::elab:endtest