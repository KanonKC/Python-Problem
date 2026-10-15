from random import randint

for i in range(5):
    with open(f"{6+i}.in", "w") as f:
        N = randint(90000,100000)
        f.write(f"{N}\n")
        for i in range(N):
            f.write(f"{randint(1, 300)}\n")