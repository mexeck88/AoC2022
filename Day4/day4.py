with open("input.txt") as f:
    inp = f.readlines()
sum = 0
for line in inp:
    range1 = []
    range2 = []
    left,right = line.strip().split(",")
    l1,r1 = left.split("-")
    l2,r2 = right.split("-")
    for x in range(int(l1),int(r1)+1):
        range1.append(x)
    for x in range(int(l2),int(r2)+1):
        range2.append(x)
    shared = set(range1).intersection(range2)
    if shared != set():
        sum += 1
    # if shared == set(range1) or shared == set(range2):
    #     sum += 1 
print(sum)  