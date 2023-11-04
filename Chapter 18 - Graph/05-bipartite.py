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