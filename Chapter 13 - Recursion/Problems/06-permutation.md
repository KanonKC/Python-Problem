# Permutation

หาผลรวมของจำนวนที่รับเข้ามา

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นสายข้อความที่เป็นจำนวนเต็มหลาย ๆ ตัว โดยแต่ละตัวจะคั่นด้วย Spacebar

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบเป็นผลรวมของจำนวนทั้งหมดที่ใส่เข้ามา

## Example 1
<pre class="output">
Enter numbers: _1 2 3_
6
</pre>

::elab:begincode blank=True
n = [int(i) for i in input("Enter numbers: ").split()]

def findSum(n):
    if len(n) == 0:
        return 0
    return n[0] + findSum(n[1:])

print(findSum(n))
::elab:endcode

::elab:begintest hint="-"
1 2 3

::elab:begintest hint="-"
290549 957523 206624

::elab:endtest
::elab:begintest hint="-"
61369 631195 584700 753166 605471 907098 805981 807423 146020

::elab:endtest
::elab:begintest hint="-"
76755 206437 752470 618304 496738 687924 452532 713397

::elab:endtest