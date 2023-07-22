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

def minor(matrix, row, col):
    minor = []
    for i in range(len(matrix)):
        if i != row:
            minor.append([])
            for j in range(len(matrix[i])):
                if j != col:
                    minor[-1].append(matrix[i][j])

    return minor

def det2D(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def cofactorMatrix(matrix):
    cofacterMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cofacterMatrix[i][j] = det2D(minor(matrix, i, j)) * (-1)**(i+j)

    return cofacterMatrix

def transpose(matrix):
    matrixB = []
    for i in range(len(matrix[0])):
        matrixB.append([])
        for j in range(len(matrix)):
            matrixB[i].append(matrix[j][i])
    return matrixB

def adjointMatrix(matrix):
    return transpose(cofactorMatrix(matrix))

def determinant(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[0][i] * det2D(minor(matrix, 0, i)) * (-1)**i
    return result

def inverseMatrix(matrix):
    adjMatrix = adjointMatrix(matrix)
    det = determinant(matrix)
    printMatrix(adjMatrix)
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix[i])):
            adjMatrix[i][j] = adjMatrix[i][j] / det
    
    return adjMatrix

matrix = createMatrix()
printMatrix(inverseMatrix(matrix))

# 7 -5 -8
# -3 -7 -2
# 0 -4 -8

# 1 2 3
# 0 2 4
# 0 0 5