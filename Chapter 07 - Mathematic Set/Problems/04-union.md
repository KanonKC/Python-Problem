# Set Union

**Union** ยูเนียนของเซต A และ B คือเซตที่ประกอบด้วยสมาชิกของเซต A หรือ B

เขียนโปรแกรมที่สามารถหายูเนียนของเซต 2 เซต

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด เป็นชุดข้อความที่คั่นด้วย Spacebar ทั้งคู่ โดยที่  
**บรรทัดที่ 1** แทนเซต A  
**บรรทัดที่ 2** แทนเซต B  

<u>ข้อมูลส่งออก</u>  
แสดงค่าของ A ∪ B

## Example 1
<pre class="output">
Enter Set A: _1 2 3 4 5_
Enter Set B: _2 4 6 8 10_
1 2 3 4 5 6 8 10 
</pre>

## Example 2
<pre class="output">
Enter Set A: _3 2 1_
Enter Set B: _1 2 3_
1 2 3 
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

def union(set1,set2):
    result = []
    for n in set1:
        if n not in result:
            result.append(n)
    for n in set2:
        if n not in result:
            result.append(n)
    return result
    

a = createSet("Enter Set A: ")
b = createSet("Enter Set B: ")
printSet(union(a,b))
::elab:endcode

::elab:begintest hint="-"
1 2 3 4 5
2 4 6 8 10

::elab:endtest

::elab:begintest hint="-"
3 2 1
1 2 3

::elab:endtest

::elab:begintest hint="-"

1 2 2 3 4

::elab:endtest

::elab:begintest hint="-"
a ks jdk l wj ksdij w0 91 28 cn901 28 4v9 284 n90 28 9nv 08 12n9 0v 8n49 08n v9 021 8
asld iwo mio mvi ompei ovai wm veoiaw opmvo ea ksdij w0 91 28 cn901 28 4v9

::elab:endtest

::elab:begintest hint="-"



::elab:endtest