def calcprioritylower(char):
    return ord(char) - 96

def calcpriorityupper(char):
    return ord(char) - 38

def calcCommon(f):
    score = 0

    for line in f:
        line = line.strip("\n")
        splitidx = int(len(line)/2)
        firsthalf, secondhalf = line[:splitidx], line[splitidx:]
        #print(firsthalf + " " + secondhalf)
        charfound = False
        for c1 in firsthalf:
            for c2 in secondhalf:
                if c1 == c2 and c1.islower():
                    #print(c2)
                    #print(calcprioritylower(c1))
                    score += calcprioritylower(c1)
                    charfound = True
                    break
                elif c1 == c2 and c1.isupper():
                    #print(c2)
                    #print(calcpriorityupper(c1))
                    score += calcpriorityupper(c1)
                    charfound = True
                    break
            if charfound:
                break
    print(score)

def calcCommonThree(f):
    score = 0
    three = 0
    rucksackArr = []
    commonChar = []
    for line in f:
        line = line.strip("\n")
        three += 1
        rucksackArr.append(line)
        if three == 3:
            #print(rucksackArr)
            i = 0
            for c1 in rucksackArr[i]:
                for c2 in rucksackArr[i+1]:
                    for c3 in rucksackArr[i+2]:
                        if c1 == c2 == c3:
                            commonChar.append(c1)
            
            #print(commonChar)
            if commonChar[0].isupper():
                score += calcpriorityupper(commonChar[0])
            elif commonChar[0].islower():
                score += calcprioritylower(commonChar[0])
            rucksackArr = []
            commonChar = []
            three = 0
    print(score)



f = open("rucksack.txt", "r")
f = f.readlines()
calcCommon(f)
calcCommonThree(f)

