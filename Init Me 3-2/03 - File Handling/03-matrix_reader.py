def matrixAdd(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrixSub(a,b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def printMatrix(res):
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}",end=" ")
        print()

filename = input("File name: ")

with open(filename) as f:
    data_list = [i.strip().split() for i in f.readlines()]
    matrix = []
    oper = []
    
    one_matrix = []
    for data in data_list:
        if data[0] == '+' or data[0] == '-':
            oper.append(data[0])
            matrix.append(one_matrix)
            one_matrix = []
        else:
            one_matrix.append([int(i) for i in data])
    matrix.append(one_matrix)

    for i in range(len(oper)):
        if oper[i] == '+':
            matrix[i+1] = matrixAdd(matrix[i],matrix[i+1])
        else:
            matrix[i+1] = matrixSub(matrix[i],matrix[i+1])

    printMatrix(matrix[-1])
