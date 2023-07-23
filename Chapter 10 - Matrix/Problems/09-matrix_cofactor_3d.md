# Cofactor Matrix

ถ้ากำหนดให้ `M(A,i,j)` คือ Minor ที่แถว `i` หลัก `j` ของ Matrix `A` จะได้ว่า `C(A,i,j)` คือ 
**Cofactor** ที่แถว `i` หลัก `j` ของ Matrix `A` โดยที่

```
C(A,i,j) = (-1)**(i+j) * M(A,i,j)
```

พูดง่าย ๆ ก็คือค่าของ Minor ที่จะคูณ -1 เข้าไป ถ้าหาก `i+j` เป็นจำนวนคี่

**Cofactor Matrix** คือ ถ้ากำหนด Matrix `A` ซึ่งเป็น Matrix จัตุรัสแล้ว `Cofactor Matrix A` ก็คือ Matrix ที่สมาชิกแถวที่ `i` หลักที่ `j` มีค่าเป็น `C(A,i,j)`

<img src="https://media.nagwa.com/268134095329/en/thumbnail_l.jpeg">

ในโจทย์ข้อนี้เราจะรับ Matrix 3x3 เข้าไป 1 ตัว จากนั้นแสดง Cofactor Matrix ตัวนั้นออกมา

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
แสดง Cofactor Matrix `A`

## Example 1
<pre class="output">
_7 -5 -8_
_-3 -7 -2_
_0 -4 -8_
  48    -24     12   
  -8    -56     28   
 -46     38    -64 
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

matrix = createMatrix()

cofacterMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        cofacterMatrix[i][j] = det2D(minor(matrix, i, j)) * (-1)**(i+j)

printMatrix(cofacterMatrix)
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