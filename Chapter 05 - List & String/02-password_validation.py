password = input("Enter a password: ")

length = len(password) >= 8
upper = False
lower = False
number = False
special = False

for i in password:
    if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
        upper = True
    elif i in "qwertyuiopasdfghjklzxcvbnm":
        lower = True
    elif i in "0123456789":
        number = True
    elif i in "!@#$%^&*":
        special = True

if not length:
    print("The password length must be greater than or equal to 8")
if not upper:
    print("The password must contain one or more uppercase characters")
if not lower:
    print("The password must contain one or more lowercase characters")
if not number:
    print("The password must contain one or more numeric values")
if not special:
    print("The password must contain one or more special characters")

if length and upper and lower and number and special:
    print("Your password is strong!")