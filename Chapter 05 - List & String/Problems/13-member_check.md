# Member Check

รับข้อความหลายๆตัวเข้ามา โดยแต่ละตัวคั่นด้วย Spacebar จากนั้นอีกบรรทัดจะรับข้อความเข้ามา 1 ตัว และตอบว่าข้อความที่พึ่งรับเข้ามาเคยอยู่ในชุดข้อความที่รับมาในบรรทัดแรกหรือไม่

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด  
บรรทัดที่ 1 รับข้อความหลายตัวเข้ามา โดยแต่ละข้อความจะคั่นด้วย Spaecbar
บรรทัดที่ 2 รับข้อความ 1 ตัวเข้ามา

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบว่า ข้อความจากบรรทัดที่ 2 มีอยู่ในบรรทัดที่ 1 หรือไม่

## Example 1
<pre class="output">
Enter some word in collection: _a b c d e_
Enter a text to be checked: _b_
'b' is in the collection.
</pre>

## Example 2
<pre class="output">
Enter some word in collection: _a b c d e_ 
Enter a text to be checked: _f_
'f' is not in the collection.
</pre>

## Example 3
<pre class="output">
Enter some word in collection: _Hello Word Text Book_
Enter a text to be checked: _Mark_
'Mark' is not in the collection.
</pre>

::elab:begincode blank=True
collection = input("Enter some word in collection: ").split()
target = input("Enter a text to be checked: ")

if target in collection:
    print(f"'{target}' is in the collection.")
else:
    print(f"'{target}' is not in the collection.")
::elab:endcode

::elab:begintest hint="-"
a b c d e
b
::elab:endtest
::elab:begintest hint="-"
a b c d e
f
::elab:endtest
::elab:begintest hint="-"
Hello Word Text Book
Mark
::elab:endtest
::elab:begintest hint="-"
Hello Word Text Book Mark
Mark
::elab:endtest
::elab:begintest hint="-"
a
A
::elab:endtest
::elab:begintest hint="-"
A
A
::elab:endtest