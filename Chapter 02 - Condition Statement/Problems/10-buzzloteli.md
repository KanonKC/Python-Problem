# Buzzloteli

เนื่องจากเด็กชายบัซซี่ชอบเตะบอลมาก เขาจึงมักนำลูกบอลมาเตะเล่นที่ใต้ตึกวิศวกรรมคอมพิวเตอร์ แต่เขามักจะถูกยามตึกต่อว่า เขาจึงหนีไปเช่าสนามฟุตบอลแห่งหนึ่ง โดยสนามฟุตบอลนั้นคิดค่าบริการดังนี้  
&nbsp;&nbsp;&nbsp;&nbsp;อัตราค่าบริการชั่วโมงละ 900 บาท  
&nbsp;&nbsp;&nbsp;&nbsp;เศษชั่วโมงที่มากกว่า 20 นาทีจะปัดเป็น 1 ชั่วโมง (เช่น 1ชั่วโมง 30 นาที คิดเป็น 2 ชั่วโมง)  
&nbsp;&nbsp;&nbsp;&nbsp;หากใช้บริการตั้งแต่ 2 ชั่วโมงขึ้นไป แต่ไม่ถึง 4 ชั่วโมง จะลดราคา 10%  
&nbsp;&nbsp;&nbsp;&nbsp;หากใช้บริการ 4 ชั่วโมง จะลดราคา 20%  
&nbsp;&nbsp;&nbsp;&nbsp;หากใช้บริการตั้งแต่ 5 ชั่วโมงขึ้นไป จะลดราคา 30%  
จงเขียนโปรแกรมเพื่อคำนวณอัตราค่าบริการเป็นจำนวนเต็ม โดยรับค่าเวลาเป็นหน่วยนาที (กำหนดให้เวลาเป็นจำนวนเต็มบวกเสมอ)

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มแทนเวลาทั้งหมดที่บัซซี่เตะบอล (หน่วยเป็นนาที)

<u>ข้อมูลส่งออก</u>  
จำนวนค่าเช่าทั้งหมด ที่ต้องจ่าย

## Example 1
<pre class="output">
How long have Buzz played ?: _390_
Total price is 4410 baht.
</pre>

## Example 2
<pre class="output">
How long have Buzz played ?: _195_
Total price is 2430 baht.
</pre>

::elab:begincode blank=True
time = int(input("How long have Buzz played ?: "))
hour = time//60
min = time%60
if min > 20:
  hour+=1
p = hour * 900
if hour>=5:
  p = p*0.7
elif hour==4:
  p = p*0.8
elif hour>=2:
  p=p*0.9
else:
  p=p
print(f"Total price is {p:.0f} baht.")
::elab:endcode

::elab:begintest hint="390"
390
::elab:endtest

::elab:begintest hint="195"
195
::elab:endtest

::elab:begintest hint="20"
20
::elab:endtest

::elab:begintest hint="21"
21
::elab:endtest

::elab:begintest hint="80"
80
::elab:endtest

::elab:begintest hint="81"
81
::elab:endtest

::elab:begintest hint="140"
140
::elab:endtest

::elab:begintest hint="141"
141
::elab:endtest

::elab:begintest hint="200"
200
::elab:endtest

::elab:begintest hint="201"
201
::elab:endtest

::elab:begintest hint="260"
260
::elab:endtest

::elab:begintest hint="261"
261
::elab:endtest

::elab:begintest hint="320"
320
::elab:endtest

::elab:begintest hint="321"
321
::elab:endtest