with open("input.txt") as f:
    inp = f.readlines()
sum = 0

one = ["V","C","D","R","Z","G","B","W"]
two = ["G","W","F","C","B","S","T","V"]
three = ["C","B","S","N","W"]
four = ["Q","G","M","N","J","V","C","P"]
five = ["T","S","L","F","D","H","B"]
six = ["J","V","T","W","M","N"]
seven = ["P","F","L","C","S","T","G"]
eight = ["B","D","Z"]
nine = ["M","N","Z","W"]

dict = {}   
dict[1] = one
dict[2] = two
dict[3] = three
dict[4] = four
dict[5] = five
dict[6] = six
dict[7] = seven
dict[8] = eight
dict[9] = nine

for line in inp:
    act = line.strip().split()
    count = act[1]
    source = act[3]
    dest = act[5]
    temphold =[]
    for i in range(int(count)):
        #dict[int(dest)].append(dict[int(source)].pop())
        temphold.append(dict[int(source)].pop())
    for i in range(int(count)):
        dict[int(dest)].append(temphold.pop())
    
sum = "".join(dict[i].pop() for i in range(1,10))
print(sum)