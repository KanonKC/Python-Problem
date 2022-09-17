s = int(input("second(s): "))

m = (s//60)%60
h = (s//3600)

print(f"{s} => {h} hour(s): {m} minute(s): {s%60} second(s)")