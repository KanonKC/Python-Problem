filename = input("File name: ")

with open(filename,'r') as f:
    data = f.readline().split()
    print(f"Count: {len(data)}")