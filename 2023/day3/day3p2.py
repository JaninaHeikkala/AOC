def checkLeft(fileArray, x, y):
    number = ""
    if x - 1 >= 0:
        if fileArray[y][x-1].isdigit():
            number = getNumber(fileArray, x-1, y)
            return True, number
        else:
            return False, number
    else:
        return False, number


def checkRight(fileArray, x, y):
    number = ""
    if x + 1 < len(fileArray[y]):
        if fileArray[y][x+1].isdigit():
            number = getNumber(fileArray, x+1, y)
            return True, number
        else:
            return False, number
    else:
        return False, number


def checkAbove(fileArray, x, y):
    number = ""
    if y - 1 >= 0:
        if fileArray[y-1][x].isdigit():
            number = getNumber(fileArray, x, y-1)
            return True, number
        else:
            return False, number
    else:
        return False, number


def checkBelow(fileArray, x, y):
    number = ""
    if y + 1 < len(fileArray[y]):
        if fileArray[y+1][x].isdigit():
            number = getNumber(fileArray, x, y+1)
            return True, number
        else:
            return False, number
    else:
        return False, number


def checkLeftUpDiagonal(fileArray, x, y):
    number = ""
    if y - 1 >= 0 and x - 1 >= 0:
        if fileArray[y-1][x-1].isdigit():
            number = getNumber(fileArray, x-1, y-1)
            return True, number
        else:
            return False, number
    else:
        return False, number


def checkRightUpDiagonal(fileArray, x, y):
    number = ""
    if y - 1 >= 0 and x + 1 < len(fileArray[y]):
        if fileArray[y-1][x+1].isdigit():
            number = getNumber(fileArray, x+1, y-1)
            return True, number
        else:
            return False, number
    else:
        return False, number


def checkLeftBelowDiagonal(fileArray, x, y):
    number = ""
    if y + 1 < len(fileArray[y]) and x - 1 >= 0:
        if fileArray[y+1][x-1].isdigit():
            number = getNumber(fileArray, x-1, y+1)
            return True, number
        else:
            return False, number
    else:
        return False, number


def checkRightBelowDiagonal(fileArray, x, y):
    number = ""
    if y + 1 < len(fileArray[y]) and x + 1 < len(fileArray[y]):
        if fileArray[y+1][x+1].isdigit():
            number = getNumber(fileArray, x+1, y+1)
            return True, number
        else:
            return False, number
    else:
        return False, number
    
def getNumber(fileArray, x, y):
    number = ""
    while fileArray[y][x].isdigit():
        x -= 1
        if x < 0:
            break
    x += 1
    while fileArray[y][x].isdigit():
        number = number + fileArray[y][x]
        x += 1
        if x >= len(fileArray[y]):
            break
    return number


with open("input.txt", "r") as f:
    fileArray = [list(line.rstrip()) for line in f]

total = 0

x = 0
y = 0

firstNumber = ""
secondNumber = ""
number = ""
adjacent = 0
isAbove = False
isBelow = False

symbols = "*"

while y < len(fileArray):
    while x < len(fileArray[y]):

        if fileArray[y][x] == "*":

            # if any of the functions above return true then a symbol is connecting
            for checkFunction in [
                checkLeft, checkRight, checkAbove, 
                checkLeftUpDiagonal, checkRightUpDiagonal, checkBelow, 
                checkLeftBelowDiagonal, checkRightBelowDiagonal
            ]:
                isAdjacent, number = checkFunction(fileArray, x, y)

                if checkFunction == checkAbove and isAdjacent:
                    isAbove = True

                if (checkFunction == checkLeftUpDiagonal or checkFunction == checkRightUpDiagonal) and isAbove:  # Add your condition here
                    continue  # skip to the next iteration

                if checkFunction == checkBelow and isAdjacent:
                    isBelow = True

                if (checkFunction == checkLeftBelowDiagonal or checkFunction == checkRightBelowDiagonal) and isBelow:  # Add your condition here
                    continue  # skip to the next iteration

                if isAdjacent:
                    if number == secondNumber:
                        print(checkFunction)
                    adjacent += 1
                    if adjacent == 1:
                        firstNumber = number
                    if adjacent == 2:
                        secondNumber = number
                    print("Symbol adjacent with number:", number)
                

        if adjacent == 2:
            print("first", firstNumber)
            print("second", secondNumber)
            total += int(firstNumber)*int(secondNumber)

        adjacent = 0

        x += 1
        number = ""
        firstNumber = ""
        secondNumber = ""
        isAbove = False
        isBelow = False

    y += 1
    x = 0

print("total: ", total)
