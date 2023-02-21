time = int(input("How long have Buzz played ?: "))
hour = time//60
min = time%60
if min > 20:
  hour+=1
p = hour * 900
if hour>=5:
  p = p*0.7
elif hour==4:
  p = p*0.8
elif hour>=2:
  p=p*0.9
else:
  p=p
print(f"Total price is {p:.0f} baht.")