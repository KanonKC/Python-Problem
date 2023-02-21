ip = input().split(".")

for i in range(4):
    if int(ip[i]) < 0 or int(ip[i]) > 255:
        print("Invalid IP Address")
        break
else:
    print("Valid IP Address")