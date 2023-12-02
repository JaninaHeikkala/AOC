#works
def isOne(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "o":
            pass
        elif charArray[i] == "n" and prevChar == "o":
            pass
        elif charArray[i] == "e" and prevChar == "n":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1

#works
def isTwo(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "t":
            pass
        elif charArray[i] == "w" and prevChar == "t":
            pass
        elif charArray[i] == "o" and prevChar == "w":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1

def isThree(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "t":
            pass
        elif charArray[i] == "h" and prevChar == "t":
            pass
        elif charArray[i] == "r" and prevChar == "h":
            pass
        elif charArray[i] == "e" and prevChar == "r":
            pass
        elif charArray[i] == "e" and prevChar == "e":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1

#works
def isFour(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "f":
            pass
        elif charArray[i] == "o" and prevChar == "f":
            pass
        elif charArray[i] == "u" and prevChar == "o":
            pass
        elif charArray[i] == "r" and prevChar == "u":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1

#works
def isFive(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "f":
            pass
        elif charArray[i] == "i" and prevChar == "f":
            pass
        elif charArray[i] == "v" and prevChar == "i":
            pass
        elif charArray[i] == "e" and prevChar == "v":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1

#works
def isSix(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "s":
            pass
        elif charArray[i] == "i" and prevChar == "s":
            pass
        elif charArray[i] == "x" and prevChar == "i":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1

#works
def isSeven(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "s":
            pass
        elif charArray[i] == "e" and prevChar == "s":
            pass
        elif charArray[i] == "v" and prevChar == "e":
            pass
        elif charArray[i] == "e" and prevChar == "v":
            pass
        elif charArray[i] == "n" and prevChar == "e":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1

#works
def isEight(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "e":
            pass
        elif charArray[i] == "i" and prevChar == "e":
            pass
        elif charArray[i] == "g" and prevChar == "i":
            pass
        elif charArray[i] == "h" and prevChar == "g":
            pass
        elif charArray[i] == "t" and prevChar == "h":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1

#works
def isNine(charArray, i):
    prevChar = ""
    while True:
        if charArray[i] == "n":
            pass
        elif charArray[i] == "i" and prevChar == "n":
            pass
        elif charArray[i] == "n" and prevChar == "i":
            pass
        elif charArray[i] == "e" and prevChar == "n":
            return True
        else:
            return False
        prevChar = charArray[i]
        i += 1


f = open("input.txt", "r")

fw = open("output.txt", "w")

firstInt = ""
lastInt = ""
total = 0
newNum = ""
lineNum = 1

for line in f:
    print(lineNum)
    line = line.rstrip()
    charArray = [char for char in line]
    print(charArray)
    i = 0
    while i < len(charArray):
        if charArray[i] == "o":
            if i + 2 < len(charArray):
                if isOne(charArray, i):
                    #i += 2
                    if firstInt == "":
                        firstInt = "1"
                    else:
                        lastInt = "1"
        elif charArray[i] == "t":
            if i + 2 < len(charArray):
                if isTwo(charArray, i):
                    #i += 2
                    if firstInt == "":
                        firstInt = "2"
                    else:
                        lastInt = "2"
            if i + 4 < len(charArray):
                if isThree(charArray, i):
                    #i += 4
                    if firstInt == "":
                        firstInt = "3"
                    else:
                        lastInt = "3"
        elif charArray[i] == "f":
            if i + 3 < len(charArray):
                if isFour(charArray, i):
                    #i += 3
                    if firstInt == "":
                        firstInt = "4"
                    else:
                        lastInt = "4"
            if i + 3 < len(charArray):
                if isFive(charArray, i):
                    #i += 3
                    if firstInt == "":
                        firstInt = "5"
                    else:
                        lastInt = "5"
        elif charArray[i] == "s":
            if i + 2 < len(charArray):
                if isSix(charArray, i):
                    #i += 2
                    if firstInt == "":
                        firstInt = "6"
                    else:
                        lastInt = "6"
            if i + 4 < len(charArray):
                if isSeven(charArray, i):
                    #i += 4
                    if firstInt == "":
                        firstInt = "7"
                    else:
                        lastInt = "7"
        elif charArray[i] == "e":
            if i + 4 < len(charArray):
                if isEight(charArray, i):
                    #i += 4
                    if firstInt == "":
                        firstInt = "8"
                    else:
                        lastInt = "8"
        elif charArray[i] == "n":
            if i + 3 < len(charArray):
                if isNine(charArray, i):
                    #i += 3
                    if firstInt == "":
                        firstInt = "9"
                    else:
                        lastInt = "9"
        elif charArray[i].isdigit():
            if firstInt == "":
                firstInt = charArray[i]
            else:
                lastInt = charArray[i]
        i += 1
    if (firstInt != "" and lastInt != ""):
        newNum += firstInt + lastInt
        print(firstInt + lastInt)
        fw.write(firstInt + lastInt + "\n")
    elif (firstInt != "" and lastInt == ""):
        newNum += firstInt + firstInt
        print(firstInt + firstInt)
        fw.write(firstInt + firstInt + "\n")
    total += int(newNum)
    firstInt = ""
    lastInt = ""
    newNum = ""
    lineNum += 1

fw.close()
