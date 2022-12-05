with open('elfreadfile.txt') as f:
    lines = f.readlines()

newlines = [element.replace('\n','0') for element in lines]
integer_lines = [int(int(element)/10) for element in newlines]
integer_lines[-1] = integer_lines[-1]*10

#print(integer_lines)

sum=0
final_list=[]
for i in integer_lines:
    if i != 0:
        sum+=i
    else:
        final_list.append(sum)
        sum=0
final_list.append(sum)

final_list.sort(reverse=True)
print(final_list)

total = final_list[0]+final_list[1]+final_list[2]
print(total)