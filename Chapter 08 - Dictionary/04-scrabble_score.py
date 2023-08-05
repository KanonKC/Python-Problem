word = input("Enter a word: ").upper()

scoresheet = {
    1 : ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'] ,
    2 : ['D', 'G'] ,
    3 : ['B', 'C', 'M', 'P'] ,
    4 : ['F', 'H', 'V', 'W', 'Y'] ,
    5 : ['K'] ,
    8 : ['J', 'X'] ,
    10 : ['Q', 'Z']
}

score = 0
for letter in word:
    for key in scoresheet:
        if letter in scoresheet[key]:
            score += key
    
print(score)