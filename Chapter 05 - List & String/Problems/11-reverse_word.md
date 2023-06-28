# Reverse World

เขียนโปรแกรมที่รับข้อความเข้ามา จากนั้นแสดงข้อความนั้นแบบย้อนกลับ  
**คำใบ้:** [Slicing String](https://www.w3schools.com/python/python_strings_slicing.asp)

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับข้อความเข้ามา

<u>ข้อมูลส่งออก</u>  
แสดงข้อความนั้น โดยเรียงอักขระจากหลังมาหน้า

## Example 1
<pre class="output">
Enter a word: _Hello World_
dlroW olleH
</pre>
## Example 2
<pre class="output">
Enter a word: _daer ot siht esreveR_
Reverse this to read
</pre>

::elab:begincode blank=True
text = input("Enter a word: ")
print(text[::-1])
::elab:endcode

::elab:begintest hint="-"
Hello World
::elab:endtest

::elab:begintest hint="-"
daer ot siht esreveR
::elab:endtest

::elab:begintest hint="-"
5
::elab:endtest

::elab:begintest hint="-"
racecar
::elab:endtest

::elab:begintest hint="-"
aslkdlwkaldlwadlkla wdoakdoks;dkl  kalwkdkapwdks;kaldkwk dkadmskdwkajdksjjdkjwak
::elab:endtest