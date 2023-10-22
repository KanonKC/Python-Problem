
def traverse(graph,u,v,visited):
    if visited[u]:
        return False
    visited[u] = 1
    if u == v:
        return True
    
    found = False
    for i in range(len(graph[u])):
        if graph[u][i] == 1:
            found = found or traverse(graph,i,v,visited)
    return found

N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))
Q = int(input("Enter number of questions: "))

graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(E):
    [u,v] = [int(i) for i in input().split()]
    graph[u][v] = 1
    graph[v][u] = 1

for _ in range(Q):
    [u,v] = [int(i) for i in input("Enter 2 nodes: ").split()]
    visited = [0 for _ in range(N)]
    if traverse(graph,u,v,visited):
        print(f"Node {u} and {v} are connected")
    else:
        print(f"Node {u} and {v} are not connected")