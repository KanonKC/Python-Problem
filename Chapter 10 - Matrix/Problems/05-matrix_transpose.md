# Matrix Transpose

รับเมทริกซ์ 1 ตัว และหา Transpose ของเมทริกซ์นั้น

<img src="https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png">

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

<u>ข้อมูลส่งออก</u>  
แสดง Transpose ของเมทริกซ์ 

## Example 1
<pre class="output">
Enter the number of rows: _3_
_1 2 3_
_4 5 6_
_7 8 9_
  1      4      7
  2      5      8
  3      6      9
</pre>

## Example 2
<pre class="output">
Enter the number of rows: _2_
_111111 1111 11_
_22 2222 222222_
111111   22
 1111   2222
  11   222222
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
matrixB = []

for i in range(len(matrixA[0])):
    matrixB.append([])
    for j in range(len(matrixA)):
        matrixB[i].append(matrixA[j][i])

printMatrix(matrixB)
::elab:endcode

::elab:begintest hint="-"
3
1 2 3
4 5 6
7 8 9
::elab:endtest

::elab:begintest hint="-"
2
111111 1111 11
22 2222 222222
::elab:endtest

::elab:begintest hint="-"
1
1
::elab:endtest

::elab:begintest hint="-"
4
1 2
1 2
1 2
1 2
::elab:endtest