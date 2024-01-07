def makeStringIntoList(lines, line_num):
    line = lines[line_num]
    line = line.rstrip()
    info_map = [int(element) for element in line.split()]
    return line, info_map

def getSeedInfo(seeds, seed_num):
    i = 0
    start_seed = 0
    range_length = 0
    start_seed_put = False
    for seed in seeds:
        while i < seed_num:
            i += 1
            continue
        if not start_seed_put:
            start_seed = seed
        else:
            range_length = seed
            break
        start_seed_put = True
    return start_seed, range_length

def createSeedsDict(seeds_int, seeds):
    i = 0
    j = 0
    while i < len(seeds_int):
        curr_seed = seeds_int[i]
        while j < seeds_int[i+1]:
            curr_seed = seeds_int[i] + j
            seeds[curr_seed] = []
            j += 1
        i += 2
        j = 0
        print(i)
    return seeds

def getCurrentSeed(seeds, seed_num):
    i = 0
    for seed in seeds:
        while i < seed_num:
            i += 1
            break
        else:
            break
    return seed

f = open("input_example.txt", "r")

seeds = {}
seed_num = 0
which_one = 0
previous_seed = 0

lines = f.readlines()
line_num = len(lines)
#print(lines)

while line_num < len(lines):
    line = lines[line_num]
    line = line.rstrip()

    if "seeds: " in line:
        line = line.replace("seeds: ", "")
        seeds_str = line.split()
        seeds_int = [int(x) for x in seeds_str]
        seeds = createSeedsDict(seeds_int, seeds)
        line_num += 2
        #line, info_map = makeStringIntoList(lines, line_num)
        continue
    #first get which number corresponds and is closest to number we are trying to match
    if "map:" in line:
        start_seed, range_length = getSeedInfo(seeds, seed_num)
    if line == "" or (" " in line and "map" not in line):
        if " " in line:
            line_num += 0
        else:
            line_num += 2
        line, info_map = makeStringIntoList(lines, line_num)
        seed = getCurrentSeed(seeds, seed_num)
        to_use = [0, 0, 0]
        if len(seeds[seed]) == 0:
            search = seed
        else:
            last_index = len(seeds[seed]) - 1
            search = seeds[seed][last_index]
        while line != "":
            if search >= info_map[1]:
                if (info_map[1] >= to_use[1]) and (info_map[1] + info_map[2] >= search):
                    to_use = info_map
            if line_num+1 < len(lines):
                line_num += 1
                #print(line_num)
                line, info_map = makeStringIntoList(lines, line_num)
            else:
                break
        #when the number is found we see so we find the matching number
        if to_use[1] + to_use[2] >= search:
            difference = search - to_use[1]
            corresponding = to_use[0] + difference
            seeds[seed].append(corresponding)
        else:
            corresponding = search
            seeds[seed].append(corresponding)

        if len(seeds[seed]) == 7:
            seed_num += 1
            line_num = 0
            previous_seed = seed
            if (seed_num == len(seeds)):
                break
        #print(lower_map)

    line_num -= 1

    print(seeds)


location = 9999999999999999999999

for key, value in seeds.items():

    last_index = len(seeds[key]) - 1
    candidate = seeds[key][last_index]
    if candidate < location:
        location = candidate


print(location)