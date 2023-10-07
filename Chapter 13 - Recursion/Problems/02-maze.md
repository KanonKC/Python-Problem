# Maze

ในโจทย์ข้อนี้เราจะจำลองแผนที่ของเขาวงกต โดยใช้แต่ละอักขระดังนี้
- `#` แทนกำแพงที่ไม่สามารถเดินผ่านได้
- `.` แทนทางที่สามารถเดินผ่านได้
- `S` แทนจุดเริ่มต้น ซึ่งเป็นจุดที่เราอยู่
- `X` แทนจุดสิ้นสุด ซึ่งเป็นจุดที่เราต้องการไปถึง  

เขียนโปรแกรมที่รับแผนที่ของเขาวงกตเข้ามาแล้วคำนวณหาว่าเราสามารถเดินผ่านไปถึงจุดสิ้นสุดได้หรือไม่

<u>ข้อมูลนำเข้า</u>  
รับเป็นข้อความเข้ามาเรื่อย ๆ จนกว่าจะกด Enter โดยไม่ใส่อะไรเลย โดยทุกบรรทัดจะใส่จำนวนอักขระที่เท่ากันเสมอ (รับประกันว่าเขาวงกตจะเป็นรูปสี่เหลี่ยมผืนผ้าแน่นอน) และประกอบด้วยอักขระ `#`, `.`, `S` `X` เท่านั้น

<u>ข้อมูลส่งออก</u>  
แสดงคำตอบว่า จากแผนที่ข้างต้นสามารถเดินจากจุด `S` ไปหาจุด `X` ได้หรือไม่

## Example 1
<pre class="output">
_#######_
_#S...X#_
_#######_
_↵_

Possible to walk from S to X
</pre>

## Example 2
<pre class="output">
_#######_
_#S.#.X#_
_#######_
_↵_

Impossible to walk from S to X
</pre>

## Example 3
<pre class="output">
_################_
_#.......#......#_
_#.......#......#_
_#...S...#..X...#_
_#.......#......#_
_#.......#......#_
_#.......#......#_
_################_
_↵_

Impossible to walk from S to X
</pre>

::elab:begincode blank=True
maze = []
visited = []

def dfs(i,j):    
    if i < 0 or j < 0 or i >= len(maze) or j >= len(maze[0]) or maze[i][j] == "#" or visited[i][j] == 1:
        return False
    elif maze[i][j] == "X":
        return True
    
    visited[i][j] = 1
    return dfs(i+1,j) or dfs(i,j+1) or dfs(i-1,j) or dfs(i,j-1)
    
while True:
    tile = input()
    if tile == "":
        break
    maze.append(tile)
    visited.append([0 for i in range(len(tile))])

si,sj = 0,0
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "S":
            si,sj = i,j
            break

if dfs(si,sj):
    print("Possible to walk from S to X")
else:
    print("Impossible to walk from S to X")
::elab:endcode

::elab:begintest hint="-"
#######
#S...X#
#######


::elab:begintest hint="-"
290549 957523 206624

::elab:endtest
::elab:begintest hint="-"
#######
#S.#.X#
#######


::elab:endtest
::elab:begintest hint="-"
################
#.......#......#
#.......#......#
#...S...#..X...#
#.......#......#
#.......#......#
#.......#......#
################


::elab:endtest

::elab:begintest hint="-"
###############
#......#......#
#......#......#
#...S..#..X...#
#......#......#
#......#......#
#......#......#
###############


::elab:endtest

::elab:begintest hint="-"
###############
#......#......#
#......#......#
#...S..#..X...#
#......#......#
#......#......#
###############


::elab:endtest

::elab:begintest hint="-"
#######
#####X#
#######
#S#####
#######


::elab:endtest

::elab:begintest hint="-"
#######
##...X#
#.#####
#S#####
#######


::elab:endtest

::elab:begintest hint="-"
#######
##.#.X#
#.#.#.#
#S.#.##
#.#.#.#


::elab:endtest

::elab:begintest hint="-"
......#
.####X#
.######
.S#####
#######


::elab:endtest

::elab:begintest hint="-"
#######
#####X.
######.
#S..#..
###...#


::elab:endtest

::elab:begintest hint="-"
.......
.....X.
.......
.S.....
.......


::elab:endtest

::elab:begintest hint="-"
.......
.....X.
.#.....
#S#....
.#.....


::elab:endtest

::elab:begintest hint="-"
SE


::elab:endtest