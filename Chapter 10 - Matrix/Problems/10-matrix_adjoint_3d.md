# Adjoint

**Adjoint** คือการนำ Matrix Cofactor มา Transpose ต่ออีกที

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/42fc09808599cf39611b7dce5fc27aa6e7bd424c">

รับ Matrix เข้ามา 1 ตัว จากนั้นแสดง Adjoint ของ Matrix นั้น  

เพื่อให้การแสดงผลลัพธ์ของ Matrix ออกมาตรงกัน ขอให้ใช้ Code ต่อไปนี้ในการแสดงผล

```python
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()
```

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 3 บรรทัด แทน Matrix `A` ขนาด 3x3

<u>ข้อมูลส่งออก</u>  
แสดง Adjoint Matrix `A`

## Example 1
<pre class="output">
_7 -5 -8_
_-3 -7 -2_
_0 -4 -8_
  48     -8    -46
 -24    -56     38
  12     28    -64
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

def det2D(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def cofactorMatrix(matrix):
    cofacterMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cofacterMatrix[i][j] = det2D(minor(matrix, i, j)) * (-1)**(i+j)

    return cofacterMatrix

def transpose(matrix):
    matrixB = []
    for i in range(len(matrix[0])):
        matrixB.append([])
        for j in range(len(matrix)):
            matrixB[i].append(matrix[j][i])
    return matrixB

matrix = createMatrix()
printMatrix(transpose(cofactorMatrix(matrix)))
::elab:endcode

::elab:begintest hint="-"
7 -5 -8
-3 -7 -2
0 -4 -8
::elab:endtest

::elab:begintest hint="-"
1 2 3
4 5 6
7 8 9
::elab:endtest

::elab:begintest hint="-"
1 1 1
1 1 1
1 1 1
::elab:endtest