f = open("input.txt", "r")

total = 0

for line in f:
    totalInLine = 0

    line = line.rstrip()

    #removing unneccessary thigns
    if "Card" in line:
        line = line.replace("Card", "")
    removeColon = line.split(":")
    line = removeColon[1]
    line = line.replace("  ", " ")

    #splitting into two lists with winning numbers and card numbers separated
    numbersSplit = line.split("|")
    winningNumbers = numbersSplit[0]
    myNumbers = numbersSplit[1]

    numbersWinningList = winningNumbers.split()
    #we now have an array of all winning numbers in line
    winningNumbers = [int(num) for num in numbersWinningList]

    numbersMyList = myNumbers.split()
    #and an array of the players numbers
    myNumbers = [int(num) for num in numbersMyList]

    print("winning nums: ", winningNumbers)
    print("my nums: ", myNumbers)

    for number in winningNumbers:
        if number in myNumbers:
            if totalInLine == 0:
                totalInLine += 1
            else:
                totalInLine = totalInLine*2
    
    print(totalInLine)
    total += totalInLine

print("total: ", total)

f.close()