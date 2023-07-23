def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()

def createMatrix():
    row = 3
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

matrix = createMatrix()

cofacterMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        cofacterMatrix[i][j] = det2D(minor(matrix, i, j)) * (-1)**(i+j)

printMatrix(cofacterMatrix)