import string
lowerdict = dict(zip(string.ascii_lowercase, range(1,27)))
upperdict = dict(zip(string.ascii_uppercase, range(27,53)))
fulldict = lowerdict | upperdict

with open('Day3Text.txt') as f:
    lines = f.readlines()
lines=[word.strip() for word in lines]

sum = 0
pt2answer = 0
for i in range(0,len(lines)):
    list1 = lines[i][:int(len(lines[i])/2)]
    list2 = lines[i][int(len(lines[i])/2):]
    sum+=fulldict[list(set(list1).intersection(list2))[0]]

print(sum)

index = 0

while index < len(lines):
    firstline = lines[index]
    secondline = lines[index+1]
    thirdline = lines[index+2]
    
    pt2answer += fulldict[list(set(firstline)&set(secondline)&set(thirdline))[0]]
    index += 3
print(pt2answer)

