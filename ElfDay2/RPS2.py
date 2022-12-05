with open('ElfText2.txt') as f:
    lines = f.readlines()

lines=[word.strip() for word in lines]   #A Rock X Gotta Lose 
print(lines)                             #B Paper Y Gotta Draw
                                         #C Scissors Z Gotta Win
score = 0                                
for i in lines:
    if i[0] == "A":
        if i[2] == "X":
            score += 3
        elif i[2] == "Y":
            score += 4
        else:
            score += 8
    elif i[0] == "B":
        if i[2] == "X":
            score += 1
        elif i[2] == "Y":
            score += 5
        else:
            score += 9
    else:
        if i[2] == "X":
            score += 2
        elif i[2] == "Y":
            score += 6
        else:
            score += 7
print(score)