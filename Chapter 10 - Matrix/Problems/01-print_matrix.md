# Print Matrix

**Matrix** คือการจัดการข้อมูลในลักษณะ แถวและหลัก ซึ่งอาจหมายถึงแถวลำดับสองมิติในทางคอมพิวเตอร์

ในโจทย์ข้อนี้เราจะจำลองการสร้าง Matrix และการแสดงผลข้อมูลใน Matrix ออกมาโดยใช้ `List` ของ Python นั่นเอง

เพื่อให้การแสดงผลลัพธ์ของ Matrix ออกมาตรงกัน ขอให้ใช้ Code ต่อไปนี้ในการแสดงผล

```python
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()
```

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1** รับค่าเป็นจำนวนเต็ม `R` แทนจำนวน "แถว" ของเมทริกซ์ โดยที่ `1 ≤ R ≤ 4`  
**บรรทัดที่ 2 ถึง R+1** จะรับเป็นสายข้อความแสดงค่าในแต่ละ "แถว" ของเมทริกซ์ โดยแต่ละค่าจะคั่นด้วย Spacebar และสามารถแปลงเป็นจำนวนเต็มได้เป็นจำนวน `C` ตัว

<u>ข้อมูลส่งออก</u>  
แสดงผลลัพธ์ของเมทริกซ์ ให้ตรงตามแบบที่กำหนดไว้

## Example 1
<pre class="output">
Enter the number of rows: _3_
_1 2 3_
_4 5 6_
_7 8 9_
  1      2      3
  4      5      6
  7      8      9
</pre>

## Example 2
<pre class="output">
Enter the number of rows: _2_
_1232 1 2_
_2 15 1111111111111_
 1232    1      2
  2      15   1111111111111
</pre>

::elab:begincode blank=True
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()

row = int(input("Enter the number of rows: "))
matrix = []

for _ in range(row):
    matrix.append([int(j) for j in input().split()])

printMatrix(matrix)
::elab:endcode

::elab:begintest hint="-"
3
1 2 3
4 5 6
7 8 9
::elab:endtest

::elab:begintest hint="-"
2
1232 1 2
2 15 1111111111111
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