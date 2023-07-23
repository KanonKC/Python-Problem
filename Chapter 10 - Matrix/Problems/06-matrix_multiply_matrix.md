# Matrix Multiply

รับเมทริกซ์ 2 ตัว และหาผลคูณของ 2 เมทริกซ์นั้น

<img src="https://miro.medium.com/v2/resize:fit:1400/1*YGcMQSr0ge_DGn96WnEkZw.png">

เพื่อให้การแสดงผลลัพธ์ของ Matrix ออกมาตรงกัน ขอให้ใช้ Code ต่อไปนี้ในการแสดงผล

```python
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()
```

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1** รับค่าเป็นจำนวนเต็ม `R1` แทนจำนวน "แถว" ของเมทริกซ์ A โดยที่ `1 ≤ R1 ≤ 4`  
**บรรทัดที่ 2 ถึง R1+1** จะรับเป็นสายข้อความแสดงค่าในแต่ละ "แถว" ของเมทริกซ์ โดยแต่ละค่าจะคั่นด้วย Spacebar และสามารถแปลงเป็นจำนวนเต็มได้เป็นจำนวน `C1` ตัว  
**บรรทัดที่ R1+2** รับค่าเป็นจำนวนเต็ม `R2` แทนจำนวน "แถว" ของเมทริกซ์ B โดยที่ `1 ≤ R2 ≤ 4`  
**บรรทัดที่ R1+3 ถึง R1+R2+4** จะรับเป็นสายข้อความแสดงค่าในแต่ละ "แถว" ของเมทริกซ์ โดยแต่ละค่าจะคั่นด้วย Spacebar และสามารถแปลงเป็นจำนวนเต็มได้เป็นจำนวน `C2` ตัว  
*(โดยที่ `R1 = C2` และ `R2 = C1` เสมอ ซึ่งก็หมายความหมาย Matrix ทั้ง 2 ตัวสามารถคูณกันได้เสมอ)*

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ของเมทริกซ์ A (Matrix) * B (Matrix)

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
  8      8      14
  23     20     38
  38     32     62
</pre>

## Example 2
<pre class="output">
Enter the number of rows: _2_
1 2 3
4 5 6
Enter the number of rows: _3_
1 2
3 4
5 6
  22     28
  49     64
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

matrixC = []
for i in range(len(matrixA)):
    matrixC.append([])
    for j in range(len(matrixB[0])):
        result = 0
        for k in range(len(matrixA[0])):
            result += matrixA[i][k] * matrixB[k][j]
        matrixC[i].append(result)

printMatrix(matrixC)

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
1 2 3
4 5 6
3
1 2
3 4
5 6
::elab:endtest

::elab:begintest hint="-"
1
1
1
5
::elab:endtest

::elab:begintest hint="-"
4
1 2 3
1 2 3
1 2 3
1 2 3
3
1 5 8 4
6 5 8 4
-1 2 6 0
::elab:endtest