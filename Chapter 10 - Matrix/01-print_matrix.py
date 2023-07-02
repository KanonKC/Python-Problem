def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()

row = int(input("Enter the number of rows: "))
matrix = []

for _ in range(row):
    matrix.append([int(j) for j in input().split()])

printMatrix(matrix)