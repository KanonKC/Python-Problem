def printBox(box):
    for i in range(len(box)):
        for j in range(len(box[0])):
            print(box[i][j],end=" ")
        print()

n = int(input())
length = (n*2)-1
box = [[0 for j in range((n*2)-1)] for i in range((n*2)-1)]

num = n

for i in range(n):
    # Right
    for j in range(length):
        if box[i][j] > 0:
            pass
        else:
            box[i][j] += num

    # Down
    for j in range(length):
        if box[j][-i-1] > 0:
            pass
        else:
            box[j][-i-1] += num

    # Left
    for j in range(length):
        if box[-i-1][j] > 0:
            pass
        else:
            box[-i-1][j] += num

    for j in range(length):
        if box[j][i] > 0:
            pass
        else:
            box[j][i] += num

    num -= 1

printBox(box)