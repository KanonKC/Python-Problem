def minus_matrix(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] -= B[i][j]
    return A

def minus_matrix_listcom(A,B): # Minus Matrix เวอร์ชั่น List Comprehension
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f'{A[i][j]:^6}', end = ' ')
        print()

A = [[1,2,3],[4,5,6],[7,8,9]]  
B = [[22,13,23],[54,43,21],[23,78,71]]

print_matrix(minus_matrix(A,B))