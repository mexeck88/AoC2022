with open("input.txt") as f:
    inp = f.read()
sum = 0

for i in range (len(inp)-14):
    sub = inp[i:i+14]
    if len(set(sub)) == len(sub):
        print(f"Found one!, {sub}, This occured at char {i+14}")



    # a = inp[i-3]
    # b = inp[i-2]
    # c = inp[i-1]
    # d = inp[i]
    # if a != b and a != c and a != d and b != c and b != d and c != d:
    #     print(f"We are at index {i} which is character {i+1}")
    #     print(a,b,c,d)
    
