# Determinant 3D-Matrix

หลังจากที่เรา Determinant สำหรับ Matrix ขนาด 2x2 ไปแล้ว ต่อไปเราจะมาลองหา Determinant สำหรับ Matrix ขนาด 3x3 กันบ้าง  

โดยเทคนิคที่เราจะนำมาใช้ในการหานั่นก็คือ [Laplace Expansion](https://en.wikipedia.org/wiki/Laplace_expansion)

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/26d1eb5c3abdac6ae65566270d6ea639378f6e96">

<img src="https://www.chilimath.com/wp-content/uploads/2018/12/the-determinant-formula-3-by-3-matrix.png">

เขียนโปรแกรมที่รับ Matrix 3x3 เข้ามา จากนั้นก็หา Determinant สำหรับ Matrix นั้น

<u>ข้อมูลนำเข้า</u>  
มีทั้งหมด 3 บรรทัด แทน Matrix `A` ขนาด 3x3

<u>ข้อมูลส่งออก</u>  
แสดง Determinant ของ Matrix `A`

## Example 1
<pre class="output">
_7 -5 -8_
_-3 -7 -2_
_0 -4 -8_
360
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

def determinant(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[0][i] * det2D(minor(matrix, 0, i)) * (-1)**i
    return result

matrix = createMatrix()
print(determinant(matrix))
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