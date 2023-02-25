filename = input("File name: ")

records = []

with open(filename,'r') as f:
    data = f.readline().split()
    for word in data:
        if word.lower().strip('.') not in records:
            records.append(word.lower().strip('.'))
    print(f"Count: {len(records)}")
    print(records)