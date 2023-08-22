[temp,unit] = input("Enter the temperature: ").split()
targetUnit = input("Enter the unit to be converted: ")

temp = float(temp)

if unit == "C":
    c = temp
elif unit == "F":
    c = (temp - 32) * 5/9
elif unit == "K":
    c = temp - 273.15
elif unit == "R":
    c = 5/4 * temp

if targetUnit == "C":
    print(f"{(c):.2f} C")
elif targetUnit == "F":
    print(f"{(c * 9/5 + 32):.2f} F")
elif targetUnit == "K":
    print(f"{(c + 273.15):.2f} K")
elif targetUnit == "R":
    print(f"{(c * 4/5):.2f} R")