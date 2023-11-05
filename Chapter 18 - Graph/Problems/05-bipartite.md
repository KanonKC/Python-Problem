# Bipartite Graph

เขียนโปรแกรมเพื่อตรวจสอบว่ากราฟ `G = (V,E)` ที่รับเข้ามาเป็น Bipartite Graph หรือไม่

<u>ข้อมูลนำเข้า</u>  
**บรรทัดที่ 1** รับเข้ามาเป็นจำนวนเต็ม `V` แทนจำนวน Node ทั้งหมดของกราฟนี้  
**บรรทัดที่ 2** รับเข้ามาเป็นจำนวนเต็ม `E` แทนจำนวน Edge ทั้งหมดของกราฟนี้  
**หลังจากนี้จำนวน `E` บรรทัด** รับเข้ามาเป็นจำนวนเต็มสองจำนวน `u` และ `v` แทนว่ามี Edge ที่เชื่อมระหว่าง Node `u` และ `v`  
*รับประกันว่าทุก Node ของ Graph สามารภเดินทางไปหากันได้ทั้งหมด*

<u>ข้อมูลส่งออก</u>  
มีบรรทัดเดียว แสดงคำตอบว่ากราฟที่รับเข้ามาเป็น Bipartite Graph หรือไม่

## Example 1
<pre class="output">
Enter number of nodes: _3_
Enter number of edges: _3_
_0 1_
_1 2_
_2 0_
Graph is not bipartite 
</pre>

## Example 2
<pre class="output">
Enter number of nodes: _4_
Enter number of edges: _3_
_0 1_
_0 2_
_3 0_
Graph is bipartite
</pre>

::elab:begincode blank=True
N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))

graph = [[0 for _ in range(N)] for _ in range(N)]


for _ in range(E):
    [u,v] = [int(i) for i in input().split()]
    graph[u][v] = 1
    graph[v][u] = 1

def bfs(graph,u):
    queue = []
    visited = [0 for _ in range(N)]
    queue.append(u)
    visited[u] = 1
    while len(queue) != 0:
        u = queue.pop(0)
        for i in range(len(graph[u])):
            if graph[u][i] == 1:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 3 - visited[u]
                elif visited[i] == visited[u]:
                    return False
    return True

if bfs(graph,0):
    print("Graph is bipartite")
else:
    print("Graph is not bipartite")
::elab:endcode

::elab:begintest hint="-"
3
3
0 1
1 2
2 0
::elab:endtest

::elab:begintest hint="-"
4
3
0 1
0 2
3 0
::elab:endtest

::elab:begintest hint="-"
8
15
0 3
3 0
0 1
2 5
5 0
0 5
5 4
4 5
5 6
6 7
7 4
4 3
3 6
6 5
5 2
::elab:endtest

::elab:begintest hint="-"
8
15
0 3
3 0
0 1
2 5
5 0
0 5
5 4
4 5
5 6
6 7
7 4
4 3
3 6
6 5
5 2
0 2
::elab:endtest

::elab:begintest hint="-"
9
11
0 1
0 5
1 6
5 6
5 4
4 8
1 7
7 8
7 2
8 3
2 3
::elab:endtest

::elab:begintest hint="-"
9
12
0 1
0 5
1 6
5 6
5 4
4 8
1 7
7 8
7 2
8 3
2 3
1 5
::elab:endtest