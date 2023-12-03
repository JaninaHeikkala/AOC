def checkLeft(fileArray, x, y):
    if x - 1 >= 0:
        if fileArray[y][x-1] in symbols:
            return True
        else:
            return False
    else:
        return False


def checkRight(fileArray, x, y):
    if x + 1 < len(fileArray[y]):
        if fileArray[y][x+1] in symbols:
            return True
        else:
            return False
    else:
        return False


def checkAbove(fileArray, x, y):
    if y - 1 >= 0:
        if fileArray[y-1][x] in symbols:
            return True
        else:
            return False
    else:
        return False


def checkBelow(fileArray, x, y):
    if y + 1 < len(fileArray[y]):
        if fileArray[y+1][x] in symbols:
            return True
        else:
            return False
    else:
        return False


def checkLeftUpDiagonal(fileArray, x, y):
    if y - 1 >= 0 and x - 1 >= 0:
        if fileArray[y-1][x-1] in symbols:
            return True
        else:
            return False
    else:
        return False


def checkRightUpDiagonal(fileArray, x, y):
    if y - 1 >= 0 and x + 1 < len(fileArray[y]):
        if fileArray[y-1][x+1] in symbols:
            return True
        else:
            return False
    else:
        return False


def checkLeftBelowDiagonal(fileArray, x, y):
    if y + 1 < len(fileArray[y]) and x - 1 >= 0:
        if fileArray[y+1][x-1] in symbols:
            return True
        else:
            return False
    else:
        return False


def checkRightBelowDiagonal(fileArray, x, y):
    if y + 1 < len(fileArray[y]) and x + 1 < len(fileArray[y]):
        if fileArray[y+1][x+1] in symbols:
            return True
        else:
            return False
    else:
        return False


with open("input.txt", "r") as f:
    fileArray = [list(line.rstrip()) for line in f]

total = 0

x = 0
y = 0

number = ""
symbolAdjacent = False

symbols = "*%@/#=-$+&"

while y < len(fileArray):
    while x < len(fileArray[y]):

        while fileArray[y][x].isdigit():

            number = number + fileArray[y][x]

            if not symbolAdjacent:
                # if any of the functions above return true then a symbol is connecting
                if any([
                    checkLeft(fileArray, x, y),
                    checkRight(fileArray, x, y),
                    checkAbove(fileArray, x, y),
                    checkBelow(fileArray, x, y),
                    checkLeftUpDiagonal(fileArray, x, y),
                    checkRightUpDiagonal(fileArray, x, y),
                    checkLeftBelowDiagonal(fileArray, x, y),
                    checkRightBelowDiagonal(fileArray, x, y)
                ]):
                    symbolAdjacent = True
                    #print("symbol adjacent")

            x += 1
            if x >= len(fileArray[y]):
                break

        if symbolAdjacent:
            total += int(number)
            #print(number)

        symbolAdjacent = False

        x += 1
        number = ""

    y += 1
    x = 0

print("total: ", total)
