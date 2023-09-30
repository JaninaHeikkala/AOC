def part1(f):

    total = 0

    for line in f:
        line = line.strip("\n")
        linesplit = line.split(',')
        elemsplit1 = linesplit[0].split('-')
        elemsplit2 = linesplit[1].split('-')
        if (int(elemsplit1[0]) <= int(elemsplit2[0])) and (int(elemsplit1[1]) >= int(elemsplit2[1])):
            total += 1
        elif (int(elemsplit1[0]) >= int(elemsplit2[0])) and (int(elemsplit1[1]) <= int(elemsplit2[1])):
            total += 1

    return total

def part2(f):
    
    total = 0

    for line in f:
        line = line.strip("\n")
        linesplit = line.split(',')
        elemsplit1 = linesplit[0].split('-')
        elemsplit2 = linesplit[1].split('-')
        if not (int(elemsplit1[1]) < int(elemsplit2[0]) or int(elemsplit2[1]) < int(elemsplit1[0])):
            total +=1

    return total


f = open("input.txt", "r")
f = f.readlines()
total1 = part1(f)
print("part1: " + str(total1))
total2 = part2(f)
print("part2: " + str(total2))
