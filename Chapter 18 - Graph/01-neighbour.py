N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))

graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(E):
    [u,v] = [int(i) for i in input().split()]
    graph[u][v] = 1
    graph[v][u] = 1

for i in range(len(graph)):
    print(f"Node #{i} has neighbours: ",end="")
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            print(j,end=" ")
    print()