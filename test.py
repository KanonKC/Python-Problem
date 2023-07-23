def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()

matrix = [
    [1,2],
    [3,4],
    [5,6]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j]*5,end=" ")
    print()