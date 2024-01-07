def makeStringIntoList(lines, line_num):
    line = lines[line_num]
    line = line.rstrip()
    try:
        info_map = [int(element) for element in line.split()]
        return line, info_map
    except:
        return line, None

def findNext(search, info_map, to_use, line_num, checked, lines, line, seeds_that_dont_exist, seeds, min_seed):
    while " " in line and "map" not in line:
        if search >= info_map[0]:
            if (info_map[0] >= to_use[0]) and (info_map[0] + info_map[2] > search):
                to_use = info_map
        line_num -= 1
        line, info_map = makeStringIntoList(lines, line_num)
        if "map" in line:
            checked += 1
            if checked == 7:
                if to_use != [0, 0, 0]:
                    search = findCorresponding(search, to_use)
                if search not in seeds_that_dont_exist and search >= min_seed:
                    seed_exists = checkIfSeedExists(search, lines, seeds)
                    return search, seed_exists, checked, line_num
                else:
                    return search, False, checked, line_num
            if to_use == [0, 0, 0]:
                continue
            else:
                search = findCorresponding(search, to_use)
    return search, False, checked, line_num

def getSeeds(lines):
    line = lines[0]
    line = line.rstrip()
    line = line.replace("seeds: ", "")
    seeds = [int(element) for element in line.split()]
    return seeds

def checkIfSeedExists(search, lines, seeds):
    curr_seed = 0
    i = 0
    while i < len(seeds):
        if (search >= seeds[i]) and (search <= (seeds[i] + seeds[i+1])):
            return True
        i += 2
    return False

def findCorresponding(search, info_map):
    i = 0
    difference = info_map[0] - info_map[1]
    search = search - difference
    return search

def getMinSeed(seeds):
    min_seed = 999999999999999999999999
    i = 0
    while i < len(seeds):
        if min_seed >= seeds[i]:
            min_seed = seeds[i]
        i += 2
    return min_seed


f = open("input.txt", "r")

location = 999999999999999999999999

lines = f.readlines()
line_num = len(lines)-1
current_location = 7961875-1
#current_location = 3030725489-1
checked = 0
search = 0
info_map = []
seeds_that_dont_exist = []
seeds = getSeeds(lines)
min_seed = getMinSeed(seeds)
stop_everything = False

while line_num < len(lines) and not stop_everything:
    to_use = [0, 0, 0]
    line, info_map = makeStringIntoList(lines, line_num)
    if line_num == len(lines)-1:
        current_location += 1
        search = current_location
        #print("checking: ", current_location)
        search, seed_exists, checked, line_num = findNext(search, info_map, to_use, line_num, checked, lines, line, seeds_that_dont_exist, seeds, min_seed)
        #print("searching: ", search)
        line, info_map = makeStringIntoList(lines, line_num)
    if ":" in lines[line_num]:
        line_num -= 1
    if " " in line and "map" not in line:
        search, seed_exists, checked, line_num = findNext(search, info_map, to_use, line_num, checked, lines, line, seeds_that_dont_exist, seeds, min_seed)
        #print("searching: ", search)
        if seed_exists == True and current_location < location:
            location = current_location
            current_location += 1
            print("found seed: ", search)
            stop_everything = True
        if checked == 7 and seed_exists == False:
            seeds_that_dont_exist.append(search)
        if checked == 7:
            print("current seed: ", search)

    line_num -= 1

    if line_num == 0:
        line_num = len(lines)-1
        checked = 0
        print("one seed checked, location: ", current_location)


print("lowest location: ", location)