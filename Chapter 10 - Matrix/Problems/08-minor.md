# Minor

**Minor** ของสมาชิก แถวที่ `i` หลักที่ `j` คือ ดีเทอร์มิแนนท์ของเมทริกซ์ตัวใหม่ที่เกิดจากการตัด แถวที่ `i` และหลักที่ `j` ของ Matrix `A` ออกไป

<img src="https://www.onlinemath4all.com/images/minorofmatq1p1.png">

เพื่อให้การแสดงผลลัพธ์ของ Matrix ออกมาตรงกัน ขอให้ใช้ Code ต่อไปนี้ในการแสดงผล

```python
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()
```

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1 - 3** จะรับเป็นสายข้อความแสดงค่าในแต่ละ "แถว" ของเมทริกซ์ โดยแต่ละค่าจะคั่นด้วย Spacebar และสามารถแปลงเป็นจำนวนเต็มได้เป็นจำนวน `3` ตัว  
*(จะเห็นว่าเราจะได้ Matrix `A` ขนาด 3x3)*  
**บรรทัดที่ 4** จำนวนเต็มอีก 2 ตัว (คั่นด้วย Spacebar) คือ `i` กับ `j` แทนแถว และหลักที่ต้องการตัดเพื่อทำ Minor ตามลำดับ

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ Minor ของ Matrix A เมื่อตัดแถวที่ `i` หลักที่ `j`

## Example 1
<pre class="output">
_1 2 3_
_4 5 6_
_7 8 9_
Enter the row and column to be sliced: _3 3_
  1      2
  4      5
</pre>

## Example 2
<pre class="output">
_1 2 3_
_4 5 6_
_7 8 9_
Enter the row and column to be sliced: _2 2_
  1      3
  7      9
</pre>

::elab:begincode blank=True
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()

def createMatrix():
    row = 3
    matrix = []

    for _ in range(row):
        matrix.append([int(j) for j in input().split()])

    return matrix

def minor(matrix, row, col):
    minor = []
    for i in range(len(matrix)):
        if i != row:
            minor.append([])
            for j in range(len(matrix[i])):
                if j != col:
                    minor[-1].append(matrix[i][j])

    return minor

matrix = createMatrix()
row,col = [int(i) for i in input("Enter the row and column to be sliced: ").split()]
printMatrix(minor(matrix, row-1, col-1))
::elab:endcode

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
3 3
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
2 2
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
1 1
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
1 2
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
1 3
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
2 1
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
2 3
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
3 1
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
3 2
::elab:endtest