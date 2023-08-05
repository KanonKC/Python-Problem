N = int(input("Number of students: "))

students = {}
totalScore = 0
for i in range(N):
    x = input().split()
    name = x[0]
    score = float(x[1])
    
    totalScore += score
    students[name] = score

averageScore = totalScore / N

print(f"Average score: {averageScore:.2f}")
print("Students with score above or equal to average:")
for name in students:
    if students[name] >= averageScore:
        print(name)