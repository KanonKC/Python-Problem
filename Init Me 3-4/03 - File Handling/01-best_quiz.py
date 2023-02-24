filename = input("File name: ")

f = open(filename).read().splitlines()
name = []
score = []

for i in f:
    i = i.split()
    for j in range(1,len(i)):
        i[j] = int(i[j])
    total_score = i[1:]
    name.append(i[0])
    score.append(sum(total_score)-max(total_score)-min(total_score))

max_score = max(score)
print(max_score)

for i in range(len(score)):
    if score[i] == max_score:
        print(name[i])
