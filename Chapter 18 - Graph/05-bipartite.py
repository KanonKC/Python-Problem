N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))

graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(E):
    [u,v] = [int(i) for i in input().split()]
    graph[u][v] = 1
    graph[v][u] = 1

def is_bipartite():
    visited = [0 for _ in range(N)]
    
    # Check all components (though problem guarantees connected graph)
    for start in range(N):
        if visited[start] == 0:
            # BFS for this component
            queue = []
            queue.append(start)
            visited[start] = 1
            
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

if is_bipartite():
    print("Graph is bipartite")
else:
    print("Graph is not bipartite")