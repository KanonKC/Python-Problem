N = int(input("Enter number of nodes: "))
E = int(input("Enter number of edges: "))
Q = int(input("Enter number of question: "))

graph = [[0 for _ in range(N)] for _ in range(N)]

print("Creating graph(s)")
for _ in range(E):
    [u,v] = [int(i) for i in input().split()]
    graph[u][v] = 1
    graph[v][u] = 1

print("Questions")
for _ in range(Q):
    node = int(input("Enter node: "))
    hasNeighbour = False
    for i in range(N):
        if graph[node][i] == 1:
            print(i)
            hasNeighbour = True
    if not hasNeighbour:
        print("This node has no neighbour")
