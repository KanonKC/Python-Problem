# Letter Count

ในโจทย์ข้อนี้เราจะมานับจำนวนตัวอักษร a-z จากบทความที่เรารับเข้ามา และแสดงออกมาว่าในบทความมีตัวอักษรแต่ละตัวกี่ตัว  

โดยที่:  
- ลำดับการแสดงตัวอักษรแต่ละตัว จะเรียงตามลำดับของอักษรที่เจอก่อน
- ให้แสดงเฉพาะตัวอักษรที่มีในบทความ
- ให้พิจารณาทุกตัวเป็นตัวพิมพ์เล็ก (lowercase) ทั้งหมด โดยเราสามารถแปลงตัวอักษรทุกตัวให้เป็นพิมพ์เล็กด้วย `.lower()` ได้ ([ดูวิธีใช้งาน](https://www.programiz.com/python-programming/methods/string/lower))

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับข้อความ/บทความเข้ามา

<u>ข้อมูลส่งออก</u>  
แสดงตัวอักษรแต่ละตัว และจำนวนที่มีในบทความนั้น

## Example 1
<pre class="output">
Enter text: _cat_
c: 1
a: 1
t: 1
</pre>

## Example 2
<pre class="output">
Enter text: _Level_
l: 2
e: 2
v: 1
</pre>

## Example 3
<pre class="output">
Enter text: _become aware of happiness once you have lost it. Then an age comes, a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, at the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. I also understood that I hadn’t reached the third age, 
in which anticipation of the loss of happiness prevents you from living._
b: 3
e: 46
c: 10
o: 30
m: 6
a: 26
w: 6
r: 12
f: 5
h: 24
p: 9
i: 24
n: 27
s: 19
y: 7
u: 9
v: 3
l: 8
t: 32
g: 7
d: 14
k: 1
x: 1
j: 1
</pre>

::elab:begincode blank=True
text = input("Enter text: ").lower()
collection = {}

for letter in text:
    if letter not in "qwertyuiopasdfghjklzxcvbnm":
        continue
    if letter in collection:
        collection[letter] += 1
    else:
        collection[letter] = 1

for letter in collection:
    print(f"{letter}: {collection[letter]}")
::elab:endcode

::elab:begintest hint="-"
cat
::elab:endtest

::elab:begintest hint="-"
Level
::elab:endtest

::elab:begintest hint="-"
become aware of happiness once you have lost it. Then an age comes, a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, at the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. I also understood that I hadn’t reached the third age, 
in which anticipation of the loss of happiness prevents you from living.
::elab:endtest

::elab:begintest hint="-"
Your only chance of survival, if you are sincerely smitten, lies in hiding this fact from the woman you love, of feigning a casual detachment under all circumstances. What sadness there is in this simple observation! What an accusation against man! However, it had never occurred to me to contest this law, nor to imagine disobeying it: love makes you weak, and the weaker of the two is oppressed, tortured and finally killed by the other, who in his or her turn oppresses, tortures and kills without having evil intentions, without even getting pleasure from it, with complete indifference; that’s what men, normally, call love.
::elab:endtest

::elab:begintest hint="-"
‘I am quite serious. Look at those kids. The boys want to get the girls into bed so they can have their corks popped off their bottles and forth. When a man blows his nose you don’t call it love. Why get all misty-eyed when a man blows another part of his anatomy? As for the girls, they’re either going along for the ride because they can get the things they want from the boys, or else maybe they enjoy being in bed too. Thought I doubt it. I never knew an eighteen-year-old boy who didn’t drop the egg off his spoon at the first fence.’
::elab:endtest

::elab:begintest hint="-"
a
::elab:endtest