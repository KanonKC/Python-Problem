from math import sqrt

walkingSequences = input("Enter walking sequences: ")

x,y = 0,0

for i in walkingSequences:
    if i == "L":
        x -= 1
    elif i == "R":
        x += 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1

distance = sqrt(x**2 + y**2)
print(f"Distance: {distance:.2f}")