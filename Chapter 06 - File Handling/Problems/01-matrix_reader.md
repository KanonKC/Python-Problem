# Matrix Reader

ไฟล์ matrix1.txt มีข้อมูลดังนี้

<pre class="output">
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
+
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
-
2 12 2 0
1 5 7 3
10 13 2 4
1 0 11 1
</pre>

เขียนโปรแกรมที่รับไฟล์ที่เหมือนกับตัวอย่างด้านบนเข้ามา จากนั้นคำนวณผลลัพธ์ที่เกิดจากการบวก(+) หรือลบ(-) กันของ Matrix แต่ละตัว

<u>ข้อมูลนำเข้า</u>  
มีบรรทัดเดียว รับเป็นข้อความแทนชื่อไฟล์ที่ต้องการเปิดอ่าน

<u>ข้อมูลส่งออก</u>  
คำนวณผลลัพธ์ของ Matrix ที่ได้

## Example 1
<pre class="output">
File name: _matrix1.txt_
  0    -10    1     4
  4     2     0     5
 -1    -3    10     8
 12    14     4    16
</pre>

::elab:begincode blank=True
def matrixAdd(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrixSub(a,b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def printMatrix(res):
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}",end=" ")
        print()

filename = input("File name: ")

with open(filename) as f:
    data_list = [i.strip().split() for i in f.readlines()]
    matrix = []
    oper = []
    
    one_matrix = []
    for data in data_list:
        if data[0] == '+' or data[0] == '-':
            oper.append(data[0])
            matrix.append(one_matrix)
            one_matrix = []
        else:
            one_matrix.append([int(i) for i in data])
    matrix.append(one_matrix)

    for i in range(len(oper)):
        if oper[i] == '+':
            matrix[i+1] = matrixAdd(matrix[i],matrix[i+1])
        else:
            matrix[i+1] = matrixSub(matrix[i],matrix[i+1])

    printMatrix(matrix[-1])

::elab:endcode

::elab:begintest hint="-"
matrix1.txt
::elab:endtest
::elab:begintest hint="-"
matrix2.txt
::elab:endtest
::elab:begintest hint="-"
matrix3.txt
::elab:endtest