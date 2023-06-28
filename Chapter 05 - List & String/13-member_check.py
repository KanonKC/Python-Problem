collection = input("Enter some word in collection: ").split()
target = input("Enter a text to be checked: ")

if target in collection:
    print(f"'{target}' is in the collection.")
else:
    print(f"'{target}' is not in the collection.")