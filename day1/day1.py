
def contains_number(string):
    return any(char.isdigit() for char in string)

f = open("calories.txt", "r")
firstCal = 0
secondCal = 0
thirdCal = 0
currentCal = 0
for line in f:
    line = line.rstrip()
    if contains_number(line):
        currentCal += int(line.replace("\n", ""))
    else:
        if currentCal >= firstCal:
            firstCal = currentCal
        elif firstCal >= currentCal >= secondCal:
            secondCal = currentCal
        elif secondCal >= currentCal >= thirdCal:
            thirdCal = currentCal
        currentCal = 0
    
print("1. " + str(firstCal))
print("2. " + str(secondCal))
print("3. " + str(thirdCal))
sum = firstCal + secondCal + thirdCal
print("sum: " + str(sum))