alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
bet = {}
for i in range(len(alpha)):
    bet[i+1] = alpha[i]

with open("input.txt","r") as f:
    inp = f.readlines()
sum = 0
for i in range(0,len(inp)-2,3):
    one,two,three = inp[i].strip(),inp[i+1].strip(),inp[i+2].strip()
    shared = "".join(set(one).intersection(two,three))
    ans = [k for k , v in bet.items() if v == shared]
    sum += ans[0]
#left,right = line[:len(line)//2],line[len(line)//2:]
#shared = "".join(set(left).intersection(right))
#ans = [k for k,v in bet.items() if v == shared]
#sum += ans[0]

print(sum)
