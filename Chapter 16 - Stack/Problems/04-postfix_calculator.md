# Postfix Calculator

เขียนโปรแกรมที่คำนวณค่าของนิพจน์ในรูปของ Postfix Notation  
โดยในการคำนวณนี้เราจะเรียงลำดับความสำคัญของตัวดำเนินการดังนี้: `หาร` > `คูณ` > `บวก` > `ลบ`

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นข้อความที่แทนนิพจน์ในรูปแบบ Postfix Notation ประกอบไปด้วยตัวเลข และตัวดำเนินการ 4 ตัวคือ `+`, `-`, `*`, `/` โดยแต่ละตัวจะคั่นกันด้วยช่องว่าง และนิพจน์ **จะไม่มีวงเล็บ**

<u>ข้อมูลส่งออก</u>  
แสดงค่าที่ได้จากการคำนวณของนิพจน์ที่รับเข้ามา โดยแสดงทศนิยม 2 ตำแหน่ง

## Example 1
<pre class="output">
Enter postfix expression: _1 2 +_
= 3.00
</pre>

## Example 2
<pre class="output">
Enter postfix expression: _1 2 3 * + 4 -_
= 3.00
</pre>

## Example 3
<pre class="output">
Enter postfix expression: _10 6 5 * 2 / + 4 -_
= 21.00
</pre>

::elab:begincode blank=True
STACK = []
pointer = -1
size = 0

def push(value):
    global pointer,size
    if pointer + 1 == size:
        size += 1
        STACK.append(value)
    else:
        STACK[pointer + 1] = value
    pointer += 1

def empty():
    global pointer
    return pointer == -1

def pop(remove=True):
    global pointer
    if pointer == -1:
        return None

    rtn = STACK[pointer]
    if remove:
        pointer -= 1
    return rtn

def show():
    global pointer
    print(STACK[:pointer+1])

operators = ["-","+","/","*"]
result = 0

expression = input("Enter postfix expression: ").split()

for char in expression:
    if char not in operators:
        push(int(char))
    else:
        op1 = pop()
        op2 = pop()
        result = 0

        if char == "-":
            result = op2 - op1
        elif char == "+":
            result = op2 + op1
        elif char == "/":
            result = op2 / op1
        elif char == "*":
            result = op2 * op1
        push(result)

print(f"= {result:.2f}")
::elab:endcode

::elab:begintest hint="-"
1 2 +
::elab:endtest
::elab:begintest hint="-"
1 2 3 * + 4 -
::elab:endtest
::elab:begintest hint="-"
10 6 5 * 2 / + 4 -
::elab:endtest
::elab:begintest hint="-"
324 8456 6541 * + 6571 618 1235 * / - 541 12354 + -
::elab:endtest
::elab:begintest hint="-"
657154156 5641541541 / 5634156654 65415461 * 5641541654 / + 5156156 + 56415641 5415641 * 45415416 / 5416541 + - 6541561 -
::elab:endtest
::elab:begintest hint="-"
1 2 + 5 6 + - 5 6 + - 9 6 + - 9 - 9 - 4 3 + 5 + -
::elab:endtest
::elab:begintest hint="-"
6 5 * 5 9 * 8 * / 7 / 8 / 6 * 1 * 2 * / 3 /
::elab:endtest