from random import randint, random

pool = ['C','F','R','K']

for i in range(10):
    print('::elab:begintest hint="-"')
    print(f"{((random()*200) - 100):.4f} {pool[randint(0,3)]}")
    print(pool[randint(0,3)])
    print('::elab:endtest')
    print()
