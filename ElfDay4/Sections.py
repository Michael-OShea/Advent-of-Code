with open('Day4Text.txt') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

sum=0
for i in range(0, len(lines)):
    A = lines[i].split(',')
    firstnums = A[0].split('-')
    secondnums = A[1].split('-')
    list1 = list(range(int(firstnums[0]),int(firstnums[1])+1))
    list2 = list(range(int(secondnums[0]),int(secondnums[1])+1))
    if all(elem in list1 for elem in list2):
        sum +=1
    elif all(elem in list2 for elem in list1):
        sum +=1
print(sum)

sum2 = 0

for i in range(0, len(lines)):
    A = lines[i].split(',')
    firstnums = A[0].split('-')
    secondnums = A[1].split('-')
    list1 = list(range(int(firstnums[0]),int(firstnums[1])+1))
    list2 = list(range(int(secondnums[0]),int(secondnums[1])+1))
    if any(elem in list1 for elem in list2):
        sum2 +=1
    elif any(elem in list2 for elem in list1):
        sum2 +=1
print(sum2)