N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))

graph = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]

for _ in range(E):
    [u,v] = [int(i) for i in input().split()]
    graph[u][v] = 1
    graph[v][u] = 1

def bfs(graph,u):
    queue = []
    queue.append(u)
    visited[u] = 1
    while len(queue) != 0:
        u = queue.pop(0)
        print(u,end=" ")
        for i in range(len(graph[u])):
            if graph[u][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = 1

bfs(graph,0)