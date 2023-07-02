def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()

def createMatrix():
    row = int(input("Enter the number of rows: "))
    matrix = []

    for _ in range(row):
        matrix.append([int(j) for j in input().split()])

    return matrix

matrixA = createMatrix()
matrixB = []

for i in range(len(matrixA[0])):
    matrixB.append([])
    for j in range(len(matrixA)):
        matrixB[i].append(matrixA[j][i])

printMatrix(matrixB)