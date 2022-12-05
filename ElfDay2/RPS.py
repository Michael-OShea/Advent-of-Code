with open('ElfText2.txt') as f:
    lines = f.readlines()

lines=[word.strip() for word in lines]   #A Rock X  
print(lines)                             #B Paper Y 
                                         #C Scissors Z 
score = 0                                
for i in lines:
    if i[0] == "A":
        if i[2] == "X":
            score += 4
        elif i[2] == "Y":
            score += 8
        else:
            score += 3
    elif i[0] == "B":
        if i[2] == "X":
            score += 1
        elif i[2] == "Y":
            score += 5
        else:
            score += 9
    else:
        if i[2] == "X":
            score += 7
        elif i[2] == "Y":
            score += 2
        else:
            score += 6
print(score)