# Palindrome

**Palindrome** คือคำ วลี จำนวนหรือลำดับที่สามารถอ่านจากหลังไปหน้าหรือหน้าไปหลังแล้วมีความหมายเหมือนกัน เช่น Racecar, Radar, Level, Civic (ลองเขียนคำเหล่านี้จากหลังมาหน้าก็จะได้คำเดิม)

เขียนโปรแกรมที่รับข้อความมา และตรวจสอบว่าเป็น Palindrome หรือไม่

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็นข้อความที่ประกอบด้วยอักขระ **a-z** เท่านั้น

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ว่าข้อความที่รับมาเป็น Palindrome หรือไม่

## Example 1
<pre class="output">
Enter a word: _racecar_
racecar is a Palindrome
</pre>

## Example 2
<pre class="output">
Enter a word: _noon_
noon is a Palindrome
</pre>

## Example 3
<pre class="output">
Enter a word: _hello_
hello is not a Palindrome
</pre>

::elab:begincode blank=True
text = input("Enter a word: ")

for i in range(len(text)//2):
    if text[i] != text[-i-1]:
        print(f"{text} is not a Palindrome")
        break
else:
    print(f"{text} is a Palindrome")
::elab:endcode

::elab:begintest hint="-"
racecar
::elab:endtest
::elab:begintest hint="-"
noon
::elab:endtest
::elab:begintest hint="-"
hello
::elab:endtest
::elab:begintest hint="-"
sakjdkwjkjkjkkdljwds
::elab:endtest
::elab:begintest hint="-"
asdfdajkljks
::elab:endtest
::elab:begintest hint="-"
saippuakivikauppias
::elab:endtest
::elab:begintest hint="-"
tattarrattat
::elab:endtest