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

def determinant(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[0][i] * det2D(minor(matrix, 0, i)) * (-1)**i
    return result

matrix = createMatrix()
print(determinant(matrix))

# 2 1 0 -3
# 0 -1 0 1
# 0 0 2 -5
# 0 0 0 1