# Prime Number

ในโจทย์ข้อนี้เราจะมาลองกับจำนวนเต็มบวกใดๆ(ค่าที่รับเข้ามาสามารถเกิน 100 ได้) และทดสอบว่าจำนวนนั้นเป็นจำนวนเฉพาะหรือไม่

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นจำนวนเต็มบวก **n** เมื่อ 1 ≤ n ≤ 1,000,000

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบออกมาว่าเป็นจำนวนเฉพาะหรือไม่

## Example 1
<pre class="output">
n: _2_
2 is a Prime Number
</pre>

## Example 2
<pre class="output">
n: _474959_
474959 is a Prime Number
</pre>

## Example 3
<pre class="output">
n: _501729_
501729 is not a Prime Number
</pre>

::elab:begincode blank=True
from math import sqrt

n = int(input("n: "))

for i in range(2,int(sqrt(n))+1):
    if n % i == 0:
        print(f"{n} is not a Prime Number")
        break
else:
    if n == 1:
        print("1 is not a Prime Number")
    else:
        print(f"{n} is a Prime Number")
::elab:endcode

::elab:begintest hint="-"
2
::elab:endtest
::elab:begintest hint="-"
3
::elab:endtest
::elab:begintest hint="-"
5
::elab:endtest
::elab:begintest hint="-"
7
::elab:endtest
::elab:begintest hint="-"
501729
::elab:endtest
::elab:begintest hint="-"
102077
::elab:endtest
::elab:begintest hint="-"
102547
::elab:endtest
::elab:begintest hint="-"
54269
::elab:endtest
::elab:begintest hint="-"
55171
::elab:endtest
::elab:begintest hint="-"
52271
::elab:endtest
::elab:begintest hint="-"
907137
::elab:endtest
::elab:begintest hint="-"
902263
::elab:endtest
::elab:begintest hint="-"
903443
::elab:endtest
::elab:begintest hint="-"
908113
::elab:endtest
::elab:begintest hint="-"
1
::elab:endtest