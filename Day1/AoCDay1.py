
with open("input.txt") as f:
    z = f.readlines()
    lines = [line.strip() for line in z]
    
elftot=[]
temptot=0

for x in lines:
    if x == '':
        elftot.append(temptot)
        temptot=0
    else:
        temptot += int(x)
print(max(elftot))
#part 2
elftot.sort(reverse=True)
print(elftot)
sum = elftot[0]+elftot[1]+elftot[2]
print(sum)