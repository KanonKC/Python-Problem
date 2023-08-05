# Scrabble Score

**สแคร็บเบิล (Scrabble)** เป็นเกมเกี่ยวกับการต่อคำชนิดหนึ่ง ที่มีผู้เล่นระหว่าง 2-4 คน ใช้ระบบการนับคะแนนโดยนับจากการสร้างคำจากการเรียงแผ่นที่มีตัวอักษรอยู่ บนกระดานขนาด 15x15 ช่อง โดยสามารถวางได้ทั้งแนวขวางและแนวดิ่ง

<img src="https://hips.hearstapps.com/hmg-prod/images/scrabble-1523476399.jpg">

โดยวิธีการได้คะแนนของเกมนี้ จะคิดจากการสร้างคำแต่ละคำ โดยแต่ละตัวอักษรของเกมนี้จะมีคะแนนไม่เท่ากัน ตามความยากในการสร้างคำ ดังนี้  

<img src="https://www.coursehero.com/qa/attachment/25860007/">

เขียนโปรแกรมที่รับคำศัพท์เข้ามา และคำนวณคะแนนของคำนั้น

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับคำศัพท์เข้ามาเป็นตัวพิมพ์ใหญ่ทั้งหมด

<u>ข้อมูลส่งออก</u>  
คะแนนที่ได้จากคำศัพท์นั้น

## Example 1
<pre class="output">
Enter a word: _HELLO_
8
</pre>

## Example 2
<pre class="output">
Enter a word: _PINEAPPLE_
15
</pre>

::elab:begincode blank=True
word = input("Enter a word: ").upper()

scoresheet = {
    1 : ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'] ,
    2 : ['D', 'G'] ,
    3 : ['B', 'C', 'M', 'P'] ,
    4 : ['F', 'H', 'V', 'W', 'Y'] ,
    5 : ['K'] ,
    8 : ['J', 'X'] ,
    10 : ['Q', 'Z']
}

score = 0
for letter in word:
    for key in scoresheet:
        if letter in scoresheet[key]:
            score += key
    
print(score)
::elab:endcode

::elab:begintest hint="-"
HELLO
::elab:endtest

::elab:begintest hint="-"
PINEAPPLE
::elab:endtest

::elab:begintest hint="-"
Serendipity
::elab:endtest

::elab:begintest hint="-"
Quixotic
::elab:endtest

::elab:begintest hint="-"
Mellifluous
::elab:endtest

::elab:begintest hint="-"
Nebulous
::elab:endtest

::elab:begintest hint="-"
Ephemeral
::elab:endtest