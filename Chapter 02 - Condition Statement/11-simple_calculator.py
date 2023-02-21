x = int(input("x: "))
oprt = input("Operator: ")
y = int(input("y: "))

if(oprt=="+"):
  print(x+y)
elif(oprt=="-"):
  print(x-y)
elif(oprt=="*"):
  print(x*y)
elif(oprt=="/"):
  print(f"{x/y:.2f}")
elif(oprt=="%"):
  print(x%y)
else:
  print("Unknown Operator")