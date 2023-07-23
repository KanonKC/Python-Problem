# Matrix Multiply Constant

รับเมทริกซ์ และจำนวนเต็ม 1 ตัว จากนั้นหาผลลัพธ์ของเมทริกซ์ที่คูณด้วย จำนวนเต็มนั้น

<img src="https://i0.wp.com/www.mathbootcamps.com/wp-content/uploads/multiply-a-matrix-and-a-scalar.jpg?w=471&ssl=1">

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
**บรรทัดที่ R+2** รับค่าเป็นจำนวนเต็ม `N`

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ของเมทริกซ์ A (Matrix) * N (Scalar)

## Example 1
<pre class="output">
Enter the number of rows: _3_
_1 2 3_
_4 5 6_
_7 8 9_
Enter the constant: _5_
  5      10     15
  20     25     30
  35     40     45
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
constant = int(input("Enter the constant: "))

for i in range(len(matrixA)):
    for j in range(len(matrixA[i])):
        matrixA[i][j] *= constant

printMatrix(matrixA)
::elab:endcode

::elab:begintest hint="-"
3
1 2 3
4 5 6
7 8 9
5
::elab:endtest

::elab:begintest hint="-"
2
11111 1111 11
22 2222 222222
10
::elab:endtest

::elab:begintest hint="-"
1
1
999
::elab:endtest

::elab:begintest hint="-"
4
1 2
1 2
1 2
1 2
8
::elab:endtest