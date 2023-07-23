# Determinant 2D-Matrix

**Determinant** คือฟังก์ชันหนึ่งที่ให้ผลลัพธ์เป็นปริมาณสเกลาร์ ซึ่งขึ้นอยู่กับค่าของ `n` ในมิติ `n×n` ของเมทริกซ์จัตุรัส `A`

สำหรับในโจทย์ข้อนี้ เราจะมาลองหา Determiant สำหรับ Matrix ขนาด 2x2 กันก่อน

<img src="https://qph.cf2.quoracdn.net/main-qimg-5056be8ce708d3c0b3cfb529eaea0d34">

เพื่อให้การแสดงผลลัพธ์ของ Matrix ออกมาตรงกัน ขอให้ใช้ Code ต่อไปนี้ในการแสดงผล

```python
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()
```

<u>ข้อมูลนำเข้า</u>   
**บรรทัดที่ 1, 2** จะรับเป็นสายข้อความแสดงค่าในแต่ละ "แถว" ของเมทริกซ์ โดยแต่ละค่าจะคั่นด้วย Spacebar และสามารถแปลงเป็นจำนวนเต็มได้เป็นจำนวน 2 ตัว  
*(จะเห็นว่าเราจะได้ Matrix ขนาด 2x2 ซึ่งเป็น Matrix จัตุรัสนั่นเอง เป็นการแสดงว่าจะหา Determinant ได้แน่นอน)*  
<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ของเมทริกซ์

## Example 1
<pre class="output">
_1 2_
_3 4_
-2
</pre>

::elab:begincode blank=True
def createMatrix():
    row = 2
    matrix = []

    for _ in range(row):
        matrix.append([int(j) for j in input().split()])

    return matrix

matrix = createMatrix()
print(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
::elab:endcode

::elab:begintest hint="-"
1 2
3 4
::elab:endtest

::elab:begintest hint="-"
1 -2
3 4
::elab:endtest

::elab:begintest hint="-"
1 -2
-3 4
::elab:endtest

::elab:begintest hint="-"
1 -2
3 -4
::elab:endtest

::elab:begintest hint="-"
-1 -2
3 -4
::elab:endtest

::elab:begintest hint="-"
1 -2
-3 -4
::elab:endtest

::elab:begintest hint="-"
-1 -2
-3 -4
::elab:endtest