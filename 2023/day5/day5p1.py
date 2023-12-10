def makeStringIntoList(lines, line_num):
    line = lines[line_num]
    line = line.rstrip()
    info_map = [int(element) for element in line.split()]
    return line, info_map

def getSeed(seeds, seed_num):
    i = 0
    for seed in seeds:
        while i < seed_num:
            i += 1
            break
        else:
            break
    return seed


f = open("input.txt", "r")

seeds = {}
line_num = 0
seed_num = 0
which_one = 0

lines = f.readlines()
#print(lines)

while line_num < len(lines):
    line = lines[line_num] 
    line = line.rstrip()

    if "seeds: " in line:
        line = line.replace("seeds: ", "")
        seeds_str = line.split()
        for seed in seeds_str:
            seeds[int(seed)] = []
        line_num += 1
        line, info_map = makeStringIntoList(lines, line_num)
    #first get which number corresponds and is closest to number we are trying to match
    if line == "" or (" " in line and "map" not in line):
        if " " in line:
            line_num += 0
        else:
            line_num += 2
        line, info_map = makeStringIntoList(lines, line_num)
        seed = getSeed(seeds, seed_num)
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

        print(seeds)

        if len(seeds[seed]) == 7:
            seed_num += 1
            line_num = 0
            if (seed_num == len(seeds)):
                break
        #print(lower_map)

    line_num += 1


location = 9999999999999999999999

for key, value in seeds.items():

    last_index = len(seeds[key]) - 1
    candidate = seeds[key][last_index]
    if candidate < location:
        location = candidate
        

print(location)