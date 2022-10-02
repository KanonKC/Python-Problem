filename = input("File name: ")
f = open(filename,"r")
cont = f.read()
text = cont.split()
sent = cont.split(".")
f.close()

for i in sent:
    if i == "":
        sent.remove(i)

print(f'There are {len(sent)} sentences and {len(text)} words.')