# Inverse 3D-Matrix

**Inverse Matrix** คือ Matrix ที่เมื่อคูณกับ Matrix ตัวเดิม จะได้ Matrix ที่มีขนาดเป็น [Identity Matrix](https://en.wikipedia.org/wiki/Identity_matrix)

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/41e7cbed13b2f1ebfd2280887ba113427c7378ff">

โดย Inverse ของ Matrix ใด ๆ นั้น สามารถหาได้จากการนำ Adjoint ของ Matrix นั้น มาหารด้วย Determinant ของ Matrix นั้น (โดยที่ Determinant จะต้องมีค่า ≠ 0 ไม่งั้นก็จะถือว่า Matrix นั้นไม่มี Inverse)

<img src="https://www.onlinemath4all.com/images/inverseofamatrix.png">

เขียนโปรแกรมที่รับ Matrix 3x3 เข้ามา จากนั้นก็หา Inverse Matrix สำหรับ Matrix นั้น

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 3 บรรทัด แทน Matrix `A` ขนาด 3x3

<u>ข้อมูลส่งออก</u>  
แสดง Inverse ของ Matrix `A`

## Example 1
<pre class="output">
_1 2 3_
_0 2 4_
_0 0 5_
 1.0    -1.0   0.2
 0.0    0.5    -0.4
 0.0    0.0    0.2
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

def adjointMatrix(matrix):
    return transpose(cofactorMatrix(matrix))

def determinant(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[0][i] * det2D(minor(matrix, 0, i)) * (-1)**i
    return result

def inverseMatrix(matrix):
    adjMatrix = adjointMatrix(matrix)
    det = determinant(matrix)
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix[i])):
            adjMatrix[i][j] = adjMatrix[i][j] / det
    
    return adjMatrix

matrix = createMatrix()
printMatrix(inverseMatrix(matrix))
::elab:endcode

::elab:begintest hint="-"
1 2 3
0 2 4
0 0 5
::elab:endtest

::elab:begintest hint="-"
7 -5 -8
-3 -7 -2
0 -4 -8
::elab:endtest

::elab:begintest hint="-"
2 9 7
4 5 6
1 5 22
::elab:endtest