# ZigZag

ภาษาซิกแซกเป็นภาษาชนิดใหม่ที่มีพื้นฐานมาจากภาษาอังกฤษ แต่มีการอ่านที่แตกต่างจากเดิม เช่น "WeAreTheChampion" หากกำหนดให้มีจำนวนแถวซิกแซกเป็น 4 จะอ่านได้ว่า `"WhpeTemiAeCaorhn"` เนื่องจากสามารถจัดเรียงตัวอักษรดังนี้ และเมื่ออ่านจากซ้ายไปขวาเรียงบรรทัดจะได้เป็นประโยคดังกล่าว

![](https://imagizer.imageshack.com/img924/4210/jvGvlx.png)

และเมื่อกำหนดจำนวนแถวซิกแซกเป็น 5 จะอ่านได้ว่า `"WCeehnAhaorTmiep"`

![](https://imagizer.imageshack.com/img924/7898/f5bJfa.png)

จงเขียนโปรแกรมเพื่อแปลงจากประโยคภาษาอังกฤษเป็นประโยคภาษาซิกแซก รับประกันว่าจำนวนแถวซิกแซกเป็นจำนวนเต็มบวก

<u>ข้อมูลนำเข้า</u>  
มี 2 บรรทัด
บรรทัดที่ 1 รับเข้ามาเป็นข้อความ
บรรทัดที่ 2 รับเข้ามาเป็นจำนวนเต็มบวก

<u>ข้อมูลส่งออก</u>  
แสดงประโยคออกมาในรูปแบบซิกแซก

## Example 1
<pre class="output">
Input sentence: _WeAreTheChampion_
Input row: _4_
WhpeTemiAeCaorhn
</pre>

## Example 2
<pre class="output">
Input sentence: _WeAreTheChampion_
Input row: _5_
WCeehnAhaorTmiep
</pre>

## Example 3
<pre class="output">
Input sentence: _YouNeverKnewHowWonderfulThatSmileCouldMakeSomeoneFeel_
Input row: _7_
YHTIeowolhudnFuewuaoMoeNnWftcaeeeKorSekmlvrnemleoedis
</pre>

::elab:begincode blank=True
s = input('Input sentence: ')
r = int(input('Input row: '))
sl = [i for i in s]
z = []
for i in range(r):
    z.append([])
def zigzag(sl,r,z):
    while len(sl) > 0:
        for i in range(r):
            if len(sl) > 0:
                z[i].append(sl[0])
                sl.pop(0)
        for k in range(r-2,0,-1):
            if len(sl) > 0:
                z[k].append(sl[0])
                sl.pop(0)
    return z

ss = ''
for a in zigzag(sl,r,z):
    for b in a:
        ss += b
print(ss)
::elab:endcode

::elab:begintest hint="test 1"
WeAreTheChampion
4
::elab:endtest

::elab:begintest hint="test 2"
WeAreTheChampion
5
::elab:endtest

::elab:begintest hint="test 3"
YouNeverKnewHowWonderfulThatSmileCouldMakeSomeoneFeel
7
::elab:endtest

::elab:begintest hint="test 1"
WeAreTheChampion
2
::elab:endtest

::elab:begintest hint="test 2"
WeAreTheChampion
4
::elab:endtest

::elab:begintest hint="test 3"
YouNeverKnewHowWonderfulThatSmileCouldMakeSomeoneFeel
10
::elab:endtest