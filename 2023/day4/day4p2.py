f = open("input.txt", "r")

total = 0
cardsDict = {}
cardNum = 1

for line in f:
    totalWonInLine = 0

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

    for number in winningNumbers:
        if number in myNumbers:
            totalWonInLine += 1

    cardsDict[cardNum] = totalWonInLine

    cardNum += 1

lines = 198

cardCopies = {}

for i in range(lines):
    cardCopies[i+1] = 1

# 1 - 198
for key in cardsDict:
    # how many wins in particular card
    # 0 -> wins
    for j in range(cardsDict[key]):
        cardCopies[key + 1 + j] += cardCopies[key]

for key, value in cardCopies.items():
    total += value
    

print("total: ", total)

f.close()