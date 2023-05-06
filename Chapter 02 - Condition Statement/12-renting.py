min = int(input("Total minute(s): "))

hour = min // 60
minl = min % 60

if minl > 20:
    hour += 1

cost = hour*100

if hour >= 2 and hour < 4: # 2 - 4 Hour
    cost = (cost * 9)/10
elif hour >= 4 and hour < 5: # 4 Hour
    cost = (cost * 8)/10
elif hour >= 5:
    cost = (cost * 7)/10

print(f"Total price is {cost:.2f} baht.")