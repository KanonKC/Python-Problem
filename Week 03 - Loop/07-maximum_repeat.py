max_char = ""
max_count = 0

current_char = ""
current_count = 0

while True:
    x = input("")
    if x == "end":
        if current_count > max_count:
            max_count = current_count
            max_char = current_char
        break
    if x == current_char:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
            max_char = current_char
        current_char = x
        current_count = 1


print(f"Most Repeat: '{max_char}' at {max_count} Count(s)")