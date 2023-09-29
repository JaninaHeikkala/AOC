def rps(whatisX, whatisY, whatisZ):

    f = open("rps.txt", "r")



    f = f.readlines()

    yTypeAdd = 0 
    xTypeAdd = 0
    zTypeAdd = 0

    #print(f)

    if whatisX == "r":
        xTypeAdd = 1
        #f = f.replace("Y", "L") #rock
        f = [f.replace("X", "L") for f in f]
        if whatisY == "p":
            yTypeAdd = 2
            #f = f.replace("X", "M") #paper
            f = [f.replace("Y", "M") for f in f]
            zTypeAdd = 3
            #f = f.replace("Z", "N") #scissors
            f = [f.replace("Z", "N") for f in f]
        elif whatisY == "s":
            yTypeAdd = 3
            #f = f.replace("Z", "N") #scissors
            f = [f.replace("Z", "N") for f in f]
            zTypeAdd = 2
            #f = f.replace("X", "M") #paper
            f = [f.replace("Y", "M") for f in f]
    elif whatisX == "p":
        xTypeAdd = 2
        #f = f.replace("Y", "M") #paper
        f = [f.replace("X", "M") for f in f]
        if whatisY == "r":
            yTypeAdd = 1
            #f = f.replace("Z", "L") #rock
            f = [f.replace("Z", "L") for f in f]
            zTypeAdd = 3
            #f = f.replace("X", "N") #scissors
            f = [f.replace("Y", "N") for f in f]
        elif whatisY == "s":
            yTypeAdd = 3
            #f = f.replace("X", "N") #scissors
            f = [f.replace("Y", "N") for f in f]
            zTypeAdd = 1
            #f = f.replace("Z", "L") #rock
            f = [f.replace("Z", "L") for f in f]
    elif whatisX == "s":
        xTypeAdd = 3
        #f = f.replace("Y", "N") #scissors
        f = [f.replace("X", "N") for f in f]
        if whatisY == "r":
            yTypeAdd = 1
            #f = f.replace("X", "L") #rock
            f = [f.replace("Y", "L") for f in f]
            zTypeAdd = 2
            #f = f.replace("Z", "M") #paper
            f = [f.replace("Z", "M") for f in f]
        elif whatisY == "p":
            yTypeAdd = 2
            #f = f.replace("Z", "M") #paper
            f = [f.replace("Z", "M") for f in f]
            zTypeAdd = 1
            #f = f.replace("X", "L") #rock
            f = [f.replace("Y", "L") for f in f]



    '''if whatisY == "rock":
        f = f.replace("Y", "L") #rock
        f = f.replace("X", "M") #paper
        f = f.replace("Z", "N") #scissors
    elif whatisY == "paper":
        f = f.replace("Y", "M") #paper
        f = f.replace("X", "N") #scissors
        f = f.replace("Z", "L") #rock
    elif whatisY == "scissors":
        f = f.replace("Y", "N") #scissors
        f = f.replace("X", "L") #rock
        f = f.replace("Z", "M") #paper'''

    score = 0

    for line in f:
        line = line.strip("\n")
        #print(line)
        if "A" in line: #rock
            if "L" in line: 
                score += xTypeAdd + 3
            elif "M" in line:
                score += yTypeAdd + 6
            elif "N" in line:
                score += zTypeAdd + 0
        if "B" in line: #paper
            if "L" in line: 
                score += xTypeAdd + 0
            elif "M" in line:
                score += yTypeAdd + 3
            elif "N" in line:
                score += zTypeAdd + 6
        if "C" in line: #scissors
            if "L" in line: 
                score += xTypeAdd + 6
            elif "M" in line:
                score += yTypeAdd + 0
            elif "N" in line:
                score += zTypeAdd + 3
    print(whatisX + whatisY + whatisZ + " " + str(score))
    f.close()

def win():

    #rock gives 1
    #paper gives 2
    #scissors gives 3

    f = open("rps.txt", "r")
    f = f.readlines()

    score = 0
    for line in f:
        line = line.strip("\n")
        if "A" in line: #rock
            if "X" in line:
                score += 3 + 0
            elif "Y" in line:
                score += 1 + 3
            elif "Z" in line:
                score += 2 + 6
        elif "B" in line: #paper
            if "X" in line:
                score += 1 + 0
            elif "Y" in line:
                score += 2 + 3
            elif "Z" in line:
                score += 3 + 6
        elif "C" in line: #scissors
            if "X" in line:
                score += 2 + 0
            elif "Y" in line:
                score += 3 + 3
            elif "Z" in line:
                score += 1 + 6

    print(score)


win()

'''rps("r", "p", "s") #13924
rps("r", "s", "p")
rps("p", "r", "s")
rps("p", "s", "r")
rps("s", "r", "p")
rps("s", "p", "r")'''