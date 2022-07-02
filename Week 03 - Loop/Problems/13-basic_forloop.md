# Basic For-Loop

เขียน For-Loop เพื่อให้ผลลัพธ์ออกตามตัวอย่างที่กำหนดให้

::elab:begincode
::elab:hide n = int(input())
::elab:endcode

## 1
<pre class="output">
0 1 2 3 4 5 6 7 8 9
</pre>
::elab:begincode
::elab:hide if n == 1:
    for i in range({{10}}):
        print(i,end=" ")
::elab:endcode

## 2
<pre class="output">
5 6 7 8 9 10
</pre>
::elab:begincode
::elab:hide elif n == 2:
    for i in range({{5,11}}):
        print(i,end=" ")
::elab:endcode

## 3
<pre class="output">
2 4 6 8 10 12 14
</pre>
::elab:begincode
::elab:hide elif n == 3:
    for i in range({{2,16,2}}):
        print(i,end=" ")
::elab:endcode

## 4
<pre class="output">
9 8 7 6 5 4 3 2 1 0
</pre>
<fieldset>
::elab:begincode
::elab:hide elif n == 4:
    for i in range({{9,-1,-1}}):
        print(i,end=" ")
::elab:endcode
</fieldset>

## 5
<pre class="output">
1 4 9 16 25 36 49 64 81 100 121 144
</pre>
::elab:begincode
::elab:hide elif n == 5:
    for i in range({{1,13}}):
        print({{i**2}},end=" ")
::elab:endcode

## 6
<pre class="output">
1 -3 5 -7 9 -11 13 -15 17 -19 21
</pre>
::elab:begincode
::elab:hide elif n == 6:
    for i in range({{11}}):
        print({{(2*i+1)*((-1)**i)}},end=" ")
::elab:endcode

::elab:begintest hint="-"
1
::elab:endtest
::elab:begintest hint="-"
2
::elab:endtest
::elab:begintest hint="-"
3
::elab:endtest
::elab:begintest hint="-"
4
::elab:endtest
::elab:begintest hint="-"
5
::elab:endtest
::elab:begintest hint="-"
6
::elab:endtest