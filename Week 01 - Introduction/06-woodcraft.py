chair = int(input("Amount of Chair: "))
table = int(input("Amount of Table: "))
storage = int(input("Amount of Storage: "))

stick = 4*chair + 6*table + 2*storage
slab  =   chair + 3*table + 2*storage
log   =           1*table + 4*storage

print(f"Stick x{stick}")
print(f"Slab x{slab}")
print(f"Log x{log}")