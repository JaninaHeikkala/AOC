

f = open("input.txt", "r")
f = f.readlines()
linenum = 0
nxt = 0

stacklist1 = []
stacklist2 = []
stacklist3 = []   
stacklist4 = []   
stacklist5 = []   
stacklist6 = []   
stacklist7 = []   
stacklist8 = []   
stacklist9 = []           

for line in f:
    linenum += 1
    if linenum >= 8:
        chars = 0
        for char in line:
            chars += 1
            if nxt == 1:
                nxt = 0
                #divide by 3? or maybe mod 3 to get which list the letter goes in
            elif char == '[':
                nxt = 1

    