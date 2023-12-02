f = open("input.txt", "r")

total = 0

number = ""
gameNum = 1

#for each line in file
for line in f:
    
    #replace things to make line easier to analyze
    line = line.rstrip()
    if "red" in line:
        line = line.replace("red", "R")
    if "green" in line:
        line = line.replace("green", "G")
    if "blue" in line:
        line = line.replace("blue", "B")
    if "Game " in line:
        line = line.replace("Game ", "")
    line = line.replace(" ", "")
    #print(line)

    #make line into array of chars
    charArray = [char for char in line]

    i = 0

    biggestRed = 0
    biggestGreen = 0
    biggestBlue = 0

    colonFound = False

    #for each char in line
    while i < len(charArray):
        #print(charArray[i])

        #check the actual relevand line info
        while charArray[i].isdigit() and colonFound == True:

            #print(charArray[i])

            #how many of the cubes are there?
            number = number + charArray[i]
            i += 1

            #print(number)

            #check what color of the cubes
            if charArray[i].isalpha():
                #print(charArray[i])
                #print(number)
                if charArray[i] == "R":
                    if int(number) > biggestRed:
                        biggestRed = int(number)
                if charArray[i] == "G":
                    if int(number) > biggestGreen:
                        biggestGreen = int(number)
                if charArray[i] == "B":
                    if int(number) > biggestBlue:
                        biggestBlue = int(number)

        number = ""

        if charArray[i] == ":":
            colonFound = True


        i += 1

    total += biggestRed * biggestGreen * biggestBlue

    gameNum += 1
        
print("total: ", total)

