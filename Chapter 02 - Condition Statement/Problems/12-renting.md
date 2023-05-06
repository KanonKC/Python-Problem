# Renting

ในการเช่าสนามฟุตบอลแห่งนึง มีการคิดค่าบริการดังนี้  

- อัตราค่าบริการชั่วโมงละ 100 บาท  
- เศษชั่วโมงที่มากกว่า 20 นาทีจะปัดเป็น 1 ชั่วโมง (เช่น 1ชั่วโมง 30 นาที คิดเป็น 2 ชั่วโมง)  
- หากใช้บริการตั้งแต่ 2 ชั่วโมงขึ้นไป แต่ไม่ถึง 4 ชั่วโมง จะลดราคา 10%  
- หากใช้บริการ 4 ชั่วโมง จะลดราคา 20%  
- หากใช้บริการตั้งแต่ 5 ชั่วโมงขึ้นไป จะลดราคา 30%  

จงเขียนโปรแกรมเพื่อคำนวณอัตราค่าบริการเป็นจำนวนเต็ม โดยรับค่าเวลาเป็นหน่วยนาที (กำหนดให้เวลาเป็นจำนวนเต็มบวกเสมอ)  

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับค่าเข้ามาเป็นจำนวนเต็มบวก แทนจำนวนนาทีที่ทำการจอง

<u>ข้อมูลส่งออก</u>  
แสดงราคาทั้งหมดที่ต้องจ่ายค่าเช่า แสดงออกเป็นทศนิยม 2 ตำแหน่ง

## Example 1
<pre class="output">
Total minute(s): _390_
Total price is 490.00 baht.
</pre>

## Example 2
<pre class="output">
Total minute(s): _195_
Total price is 270.00 baht.
</pre>


::elab:begincode blank=True
min = int(input("Total minute(s): "))

hour = min // 60
minl = min % 60

if minl > 20:
    hour += 1

cost = hour*100

if hour >= 2 and hour < 4: # 2 - 4 Hour
    cost = (cost * 9)/10
elif hour >= 4 and hour < 5: # 4 Hour
    cost = (cost * 8)/10
elif hour >= 5:
    cost = (cost * 7)/10

print(f"Total price is {cost:.2f} baht.")
::elab:endcode



::elab:begintest hint="-"
390
::elab:endtest
::elab:begintest hint="-"
195
::elab:endtest
::elab:begintest hint="-"
20
::elab:endtest
::elab:begintest hint="-"
21
::elab:endtest
::elab:begintest hint="-"
80
::elab:endtest
::elab:begintest hint="-"
81
::elab:endtest
::elab:begintest hint="-"
140
::elab:endtest
::elab:begintest hint="-"
141
::elab:endtest
::elab:begintest hint="-"
200
::elab:endtest
::elab:begintest hint="-"
201
::elab:endtest
::elab:begintest hint="-"
260
::elab:endtest
::elab:begintest hint="-"
261
::elab:endtest
::elab:begintest hint="-"
320
::elab:endtest
::elab:begintest hint="-"
321
::elab:endtest
