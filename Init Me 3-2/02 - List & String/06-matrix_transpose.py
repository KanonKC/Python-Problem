def transpose_matrix(A):
    transMat = []
    for i in range(len(A[0])): #3
        transList = []
        for j in range(len(A)): #2
            transList.append(A[j][i])
        transMat.append(transList) 
    return transMat

def transpose_matrix_listcom(A): # Transpose Matrix เวอร์ชั่น List Comprehension
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()
 
A = [
    [1,2],
    [3,4],
    [5,6]
]

print_matrix(transpose_matrix(A))