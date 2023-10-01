s = input('Input sentence: ')
r = int(input('Input row: '))
sl = [i for i in s]
z = []
for i in range(r):
    z.append([])
def zigzag(sl,r,z):
    while len(sl) > 0:
        for i in range(r):
            if len(sl) > 0:
                z[i].append(sl[0])
                sl.pop(0)
        for k in range(r-2,0,-1):
            if len(sl) > 0:
                z[k].append(sl[0])
                sl.pop(0)
    return z

ss = ''
for a in zigzag(sl,r,z):
    for b in a:
        ss += b
print(ss)