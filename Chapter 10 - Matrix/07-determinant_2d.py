def createMatrix():
    row = int(input("Enter the number of rows: "))
    matrix = []

    for _ in range(row):
        matrix.append([int(j) for j in input().split()])

    return matrix

matrix = createMatrix()
print(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])