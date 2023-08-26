# Double Palindrome

**Palindrome** คือคำที่มีลำดับของอักขระเรียงจากซ้ายไปขวา และขวาไปซ้ายมายังตำแหน่งกึ่งกลางของคำนั้นอยู่ในลักษณะสมมาตรกัน เช่น ABA,ABBA,ABAABA,ABABABA  

**Double Palindrome** คือการที่นำคำที่เป็นพาลินโดรมมาแบ่งครึ่งแล้วคำที่แบ่งออกมาทั้งสองคำเป็นพาลินโดรมด้วย เช่น QEEQQEEQ เมื่อแบ่งครึ่งจะได้คำว่า QEEQ และ QEEQ ซึ่งยังเป็นพาลินโดรมอยู่จึงจะได้ว่าคำๆนี้เป็นพาลินโดรมสองชั้นแต่คำว่า ABBA เป็นพาลินโดรมเพราะว่าเมื่อตัดแบ่งครึ่งแล้วจะได้คำว่า AB และ BA ซึ่งไม่เป็นพาลินโดรมนั่นเอง

จงเขียนโปรแกรมเพื่อหาว่าคำนั้นเป็นพาลินโดรม พาลินโดรมสองชั้น หรือไม่เป็นพาลินโดรม

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเข้ามาเป็นข้อความ

<u>ข้อมูลส่งออก</u>  
แสดงผลว่าคำนั้นเป็น Palindrome, Double Palindrome หรือไม่เป็น Palindrome

**Hint:** ใช้ฟังก์ชัน `.upper()` เพื่อแปลงอักขระเป็นตัวพิมพ์ใหญ่ทั้งหมด

## Example 1
<pre class="output">
Text: _A72Bb27A_
Palindrome
</pre>

## Example 2
<pre class="output">
Text: _AB4_
No
</pre>

## Example 3
<pre class="output">
Text: _aB3Ba5ab3BA_
Double Palindrome
</pre>

::elab:begincode blank=True
text = input('Text: ')
text = [i.upper() for i in text]

s1 = text[:len(text)//2]
if len(text)%2 == 0:
  s2 = text[len(text)//2:]
else:
  s2 = text[len(text)//2+1:]
if s1 == s1[::-1] and s2 == s2[::-1] and len(text) > 3:
  print('Double Palindrome')
elif text == text[::-1]:
  print('Palindrome')
else:
  print('No')
::elab:endcode

::elab:begintest hint=""
A72Bb27A
::elab:endtest

::elab:begintest hint=""
AB4
::elab:endtest

::elab:begintest hint=""
aB3Ba5ab3BA
::elab:endtest

::elab:begintest hint=""
dog
::elab:endtest

::elab:begintest hint=""
Ea454Ae
::elab:endtest

::elab:begintest hint=""
Fug89009guF
::elab:endtest

::elab:begintest hint=""
ABBA
::elab:endtest

::elab:begintest hint=""
12677621
::elab:endtest