s=int(input("Input starting food (S): "))
p=int(input("Input Paun's eating rate (P): "))
n=int(input("Input Gane's eating rate (n): "))
pe=s//p
ge=(s-(p*pe))//n
dog=s-(p*pe)-(ge*n)
print(f"Paun eats {pe} time(s)")
print(f"Gane eats {ge} time(s)")
print(f"Remaining {dog} for dog")