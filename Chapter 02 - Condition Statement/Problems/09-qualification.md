# Qualification

เด็กชายบุซซี่มีความฝันอยากเป็นนักฟุตบอลอาชีพ หลังจากฝึกซ้อมฟุตบอลที่สนามเช่าอย่างเต็มที่แล้ว เขาจึงไปเข้าคัดตัวกับสโมสร นครราชสีมา F.C. ในขั้นแรกจะมีการตรวจร่างกายก่อน และหนึ่งในนั้นมีการวัดค่า BMI โดยมีเกณฑ์ดังนี้

<table style="border-spacing: 5px">
<tr>
<th>เกณฑ์ค่า BMI</th>
<th>ผลการประเมิน</th>
</tr>
<tr>
<td>ตั้งแต่ 30 ขึ้นไป</th>
<td>You're in the obese range.</th>
</tr>
<tr>
<td>ตั้งแต่ 25 ขึ้นไป แต่น้อยกว่า 30</th>
<td>You're in the overweight range.</th>
</tr>
<tr>
<td>ตั้งแต่ 18.6 ขึ้นไป แต่น้อยกว่า 25</th>
<td>You're in the healthy weight range.</th>
</tr>
<tr>
<td>น้อยกว่า 18.6</th>
<td>You're in the underweight range.</th>
</tr>
</table> 

จงเขียนโปรแกรมที่รับค่า ส่วนสูง และน้าหนัก แล้วคำนวณค่า BMI แล้วแสดงผลลัพธ์ตามเกณฑ์

&nbsp;&nbsp;&nbsp;&nbsp;\( BMI=Weight (kg)./(Height (m).)^2 \)

## Example 1
<pre class="output">
Weight: _57_
Height: _165_
Your BMI is 20.9 You're in the healthy weight range.
</pre>

## Example 2
<pre class="output">
Weight: _92_
Height: _175_
Your BMI is 30.0 You're in the obese range.
</pre>

::elab:begincode blank=True
w = int(input('Weight: '))
h = int(input('Height: '))
bmi = w/(h/100)**2
if bmi>=30:
    print(f'Your BMI is {bmi:.1f} You\'re in the obese range.')
elif bmi>=25 and bmi<30:
    print(f'Your BMI is {bmi:.1f} You\'re in the overweight range.')
elif bmi>=18.6 and bmi<25:
    print(f'Your BMI is {bmi:.1f} You\'re in the healthy weight range.')
elif bmi<18.6:
    print(f'Your BMI is {bmi:.1f} You\'re in the underweight range.')
::elab:endcode

::elab:begintest hint="57 165"
57
165
::elab:endtest

::elab:begintest hint="92 175"
92
175
::elab:endtest

::elab:begintest hint="88 185"
88
185
::elab:endtest

::elab:begintest hint="50 185"
50
185
::elab:endtest

<style>
th, td {
  padding: 0px 10px 0px 10px;
  text-align:left;
}
</style>