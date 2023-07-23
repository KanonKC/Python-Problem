# Matrix Minus

รับเมทริกซ์ 2 ตัวที่มีมิติเท่ากันเสมอ และหาผลลบของ 2 เมทริกซ์นั้น

เพื่อให้การแสดงผลลัพธ์ของ Matrix ออกมาตรงกัน ขอให้ใช้ Code ต่อไปนี้ในการแสดงผล

```python
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()
```

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1** รับค่าเป็นจำนวนเต็ม `R` แทนจำนวน "แถว" ของเมทริกซ์ A โดยที่ `1 ≤ R ≤ 4`  
**บรรทัดที่ 2 ถึง R+1** จะรับเป็นสายข้อความแสดงค่าในแต่ละ "แถว" ของเมทริกซ์ โดยแต่ละค่าจะคั่นด้วย Spacebar และสามารถแปลงเป็นจำนวนเต็มได้เป็นจำนวน `C` ตัว  
**บรรทัดที่ R+2** รับค่าเป็นจำนวนเต็ม `R` แทนจำนวน "แถว" ของเมทริกซ์ B โดยที่ `1 ≤ R ≤ 4`  
**บรรทัดที่ R+3 ถึง 2R+2** จะรับเป็นสายข้อความแสดงค่าในแต่ละ "แถว" ของเมทริกซ์ โดยแต่ละค่าจะคั่นด้วย Spacebar และสามารถแปลงเป็นจำนวนเต็มได้เป็นจำนวน `C` ตัว  
*(เมทริกซ์ทั้ง 2 ตัวที่รับเข้ามา มีขนาดแถวและหลักเท่ากันเสมอ)*

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ของเมทริกซ์ A-B

## Example 1
<pre class="output">
Enter the number of rows: _3_
_1 2 3_
_4 5 6_
_7 8 9_
Enter the number of rows: _3_
_2 1 4_
_3 2 2_
_0 1 2_
  -1     1      -1
  1      3      4
  7      7      7
</pre>

::elab:begincode blank=True
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()

def createMatrix():
    row = int(input("Enter the number of rows: "))
    matrix = []

    for _ in range(row):
        matrix.append([int(j) for j in input().split()])

    return matrix

matrixA = createMatrix()
matrixB = createMatrix()

for i in range(len(matrixA)):
    for j in range(len(matrixA[i])):
        matrixA[i][j] -= matrixB[i][j]

printMatrix(matrixA)
::elab:endcode

::elab:begintest hint="-"
3
1 2 3
4 5 6
7 8 9
3
2 1 4
3 2 2
0 1 2
::elab:endtest

::elab:begintest hint="-"
2
11111 1111 11
22 2222 222222
2
444 231 21
323 54 1
::elab:endtest

::elab:begintest hint="-"
1
1
1
1
::elab:endtest

::elab:begintest hint="-"
4
1 2
1 2
1 2
1 2
4
1 2
1 2
1 2
1 2
::elab:endtest