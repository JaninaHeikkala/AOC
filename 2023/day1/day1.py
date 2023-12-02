f = open("input.txt", "r")

fw = open("outputv2.txt", "w")


firstInt = ""
lastInt = ""
total = 0
newNum = ""
lineNum = 1

for line in f:
    line = line.rstrip()

    if "one" in line:
        line = line.replace("one", "o1ne")
    if "two" in line:
        line = line.replace("two", "t2wo")
    if "three" in line:
        line = line.replace("three", "t3hree")
    if "four" in line:
        line = line.replace("four", "f4our")
    if "five" in line:
        line = line.replace("five", "f5ive")
    if "six" in line:
        line = line.replace("six", "s6ix")
    if "seven" in line:
        line = line.replace("seven", "s7even")
    if "eight" in line:
        line = line.replace("eight", "e8ight")
    if "nine" in line:
        line = line.replace("nine", "n9ine")

    charArray = [char for char in line]
    i = 0
    while i < len(charArray):
        
        if charArray[i].isdigit():
            if firstInt == "":
                firstInt = charArray[i]
            else:
                lastInt = charArray[i]
        i += 1
    if (firstInt != "" and lastInt != ""):
        newNum += firstInt + lastInt
        fw.write(firstInt + lastInt + "\n")
    elif (firstInt != "" and lastInt == ""):
        newNum += firstInt + firstInt
        fw.write(firstInt + firstInt + "\n")
    total += int(newNum)
    firstInt = ""
    lastInt = ""
    newNum = ""
    lineNum += 1
    


fw.close()


print("total: ", total)