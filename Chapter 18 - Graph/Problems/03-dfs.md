# Graph Traversal: Depth First Search

เขียนโปรแกรมการท่องไปในกราฟด้วยวิธี Depth First Search (DFS) โดยเราจะเริ่มท่องจาก Node 0 และในการเดินทางแต่ละครั้งจะเลือกเดินไปหา Node เพื่อนบ้านที่มีลำดับน้อยสุดก่อนเสมอ

<img src="https://i.ibb.co/q5RR5KZ/IMG-2360.jpg
">

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1** รับเข้ามาเป็นจำนวนเต็ม `V` แทนจำนวน Node ทั้งหมดของกราฟนี้  
**บรรทัดที่ 2** รับเข้ามาเป็นจำนวนเต็ม `E` แทนจำนวน Edge ทั้งหมดของกราฟนี้  
**หลังจากนี้จำนวน `E` บรรทัด** รับเข้ามาเป็นจำนวนเต็มสองจำนวน `u` และ `v` แทนว่ามี Edge ที่เชื่อมระหว่าง Node `u` และ `v`

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดง Node ทั้งหมดที่ผ่านการท่องกราฟแบบ DFS ตามลำดับ

## Example 1
<pre class="output">
Enter number of nodes: _6_
Enter number of edges: _8_
_0 2_
_0 4_
_0 5_
_1 4_
_1 5_
_2 3_
_2 4_
_4 5_
0 2 3 4 1 5
</pre>

::elab:begincode blank=True
N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))

graph = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]

for _ in range(E):
    [u,v] = [int(i) for i in input().split()]
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(graph,u):
    if visited[u]:
        return
    visited[u] = 1
    print(u,end=" ")
    for i in range(len(graph[u])):
        if graph[u][i] == 1:
            dfs(graph,i)

dfs(graph,0)
::elab:endcode

::elab:begintest hint="-"
6
8
0 2
0 4
0 5
1 4
1 5
2 3
2 4
4 5
::elab:endtest

::elab:begintest hint="-"
10
9
0 1
4 1
1 5
5 6
0 2
2 7
0 3
3 9
8 3
::elab:endtest

::elab:begintest hint="-"
6
5
0 2
0 5
2 3
2 4
5 1
::elab:endtest

::elab:begintest hint="-"
27
44
0 1
1 3
3 5
5 2
3 6
6 4
16 25
25 5
5 15
0 22
22 21
21 24
24 20
20 19
19 17
17 18
18 7
15 16
16 18
18 14
13 1
12 1
1 11
11 0
2 3
3 0
0 6
6 9
9 0
0 23
10 9
9 8
8 23
23 26
22 24
24 23
26 20
20 6
25 22
13 15
1 15
5 1
1 4
4 10
::elab:endtest