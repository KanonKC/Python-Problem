N = int(input("Enter the number of people: "))
treasure = {}

for i in range(N):
    favouriteList = input(f"Person #{i+1} preference list: ").split()

    for item in favouriteList:
        if item in treasure:
            treasure[item] += 1
        else:
            treasure[item] = 1

for item in treasure:
    if treasure[item] == max(treasure.values()):
        print(f"The best pick is {item}")
        break