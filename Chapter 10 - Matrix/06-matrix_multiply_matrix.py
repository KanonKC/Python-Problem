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
matrixB = createMatrix()

matrixC = []
for i in range(len(matrixA)):
    matrixC.append([])
    for j in range(len(matrixB[0])):
        result = 0
        for k in range(len(matrixA[0])):
            result += matrixA[i][k] * matrixB[k][j]
        matrixC[i].append(result)

printMatrix(matrixC)
