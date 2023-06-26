# Set Difference

**Difference** ผลต่างของเซต A และ B คือเซตที่ประกอบด้วยสมาชิกที่เปีนสมาชิกของเซต A แต่ไม่เป็นสมาชิกของเซต B

เขียนโปรแกรมที่สามารถหาผลต่างของเซต 2 เซต

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นชุดข้อความที่คั่นด้วย Spacebar ทั้งคู่ โดยที่  
**บรรทัดที่ 1** แทนเซต A  
**บรรทัดที่ 2** แทนเซต B  

<u>ข้อมูลส่งออก</u>  
แสดงค่าของ Set A - Set B

## Example 1
<pre class="output">
Enter Set A: _1 2 3 4 5_
Enter Set B: _2 4 6_
1 3 5 
</pre>

## Example 2
<pre class="output">
Enter Set A: _1 2 3 4 5_
Enter Set B: _6 7 8 9 10_
1 2 3 4 5 
</pre>

## Example 3
<pre class="output">
Enter Set A: _1 2 3_
Enter Set B: _4 5 2 1 3_

</pre>

::elab:begincode blank=True
def createSet(label):
    numbers = input(label).split()
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

def printSet(set):
    for item in set:
        print(item, end=" ")

def minus(set1,set2):
    result = []
    for n in set1:
        if n not in set2:
            result.append(n)
    return result

a = createSet("Enter Set A: ")
b = createSet("Enter Set B: ")

printSet(minus(a,b))
::elab:endcode

::elab:begintest hint="-"
1 2 3 4 5
2 4 6

::elab:endtest

::elab:begintest hint="-"
1 2 3 4 5
6 7 8 9 10

::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 2 1 3

::elab:endtest

::elab:begintest hint="-"
1 1 1 2 2 3 4 5
1 2 3
::elab:endtest

::elab:begintest hint="-"
1 2 3
1 1 1 2 2 3 4 5
::elab:endtest

::elab:begintest hint="-"
d1 2 ue90 vn 9b2 82930 vc5n9 38n2v5 0829cn 820n4 39c 90c82 90c3 8n9e 9ci
cn8 3c908 12n 90c 90c82 8301 8nc 9dic0 1v 9runv9 01ubr9 ub39 vc5n9 082
::elab:endtest