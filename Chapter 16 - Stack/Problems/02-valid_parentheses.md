# Valid Parentheses

รับค่าสตริงที่ประกอบด้วยวงเล็บ`()` ปีกกา`{}` และวงเล็บเหลี่ยม`[]` ตรวจสอบว่ามีการวางลำดับของวงเล็บที่ถูกต้องหรือไม่ โดยสตริงที่ถูกต้องจะต้องปิดวงเล็บทุกตัวที่เปิดไว้ และต้องปิดวงเล็บที่เปิดไว้ล่าสุดก่อน

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว เป็นสายข้อความที่ประกอบด้วย `(`, `)`, `{`, `}`, `[`, `]` เท่านั้น

<u>ข้อมูลส่งออก</u>  
ตรวจสอบว่ามีการวางลำดับของวงเล็บที่ถูกต้องหรือไม่

## Example 1
<pre class="output">
Enter parentheses: _{()()}_  
Valid
</pre>

## Example 2
<pre class="output">
Enter parentheses: _{(})_
Invalid
</pre>

## Example 3
<pre class="output">
Enter parentheses: _{[()]()}_
Valid
</pre>

## Example 4
<pre class="output">
Enter parentheses: _(((()))]_
Invalid
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

text = input("Enter parentheses: ")

openParen = ["(","[","{"]
closeParen = [")","]","}"]
pairParen = {
    ")":"(",
    "]":"[",
    "}":"{"
}

for paren in text:
    if paren in openParen:
        push(paren)
    elif paren in closeParen:
        if pop(False) != pairParen[paren]:
            print("Invalid")
            break
        else:
            pop()
else:
    if empty():
        print("Valid")
    else:
        print("Invalid")
::elab:endcode

::elab:begintest hint="-"
{()()}
::elab:endtest
::elab:begintest hint="-"
{(})
::elab:endtest
::elab:begintest hint="-"
{[()]()}
::elab:endtest
::elab:begintest hint="-"
(((()))]
::elab:endtest
::elab:begintest hint="-"
(
::elab:endtest
::elab:begintest hint="-"
(}
::elab:endtest
::elab:begintest hint="-"
([{[{([{}]){}}][]}()])
::elab:endtest
::elab:begintest hint="-"
)
::elab:endtest
::elab:begintest hint="-"
)(
::elab:endtest