#CHATGPT

def makeStringIntoList(line):
    line = line.rstrip()
    try:
        info_map = [int(element) for element in line.split()]
        return line, info_map
    except:
        return line, None

def checkIfSeedExists(search, seed_ranges):
    for start, end in seed_ranges:
        if start <= search <= end:
            return True
    return False

def findCorresponding(search, info_map):
    difference = info_map[0] - info_map[1]
    return search - difference

def getMaxLocation(lines, line_num):
    max_location = 0
    while line_num >= 0:
        line, info_map = makeStringIntoList(lines[line_num])
        if info_map is not None and len(info_map) >= 3 and info_map[0] + info_map[2] >= max_location:
            max_location = info_map[0] + info_map[2]
        line_num -= 1
    return max_location


def getMinSeed(seeds):
    return min(seeds[::2])

def getSeeds(lines):
    line = lines[0]
    line = line.rstrip()
    line = line.replace("seeds: ", "")
    seeds = [int(element) for element in line.split()]
    return seeds

def findNext(search, info_map, to_use, line_num, checked, lines, line, seeds_that_dont_exist, seeds, seed_ranges, min_seed):
    while " " in line and "map" not in line:
        if search >= info_map[0]:
            if (info_map[0] >= to_use[0]) and (info_map[0] + info_map[2] > search):
                to_use = info_map
        line_num -= 1

        # Pass the correct line to makeStringIntoList
        line, info_map = makeStringIntoList(lines[line_num])

        if "map" in line:
            checked += 1
            if checked == 7:
                if to_use != [0, 0, 0]:
                    search = findCorresponding(search, to_use)
                if search not in seeds_that_dont_exist and search >= min_seed:
                    seed_exists = checkIfSeedExists(search, seed_ranges)
                    return search, seed_exists, checked, line_num
                else:
                    return search, False, checked, line_num
            if to_use == [0, 0, 0]:
                continue
            else:
                search = findCorresponding(search, to_use)
    return search, False, checked, line_num

def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    location = float('inf')
    current_location = 0
    checked = 0
    search = 0
    line_num = len(lines) - 1
    seeds_that_dont_exist = set()
    seeds = getSeeds(lines)
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    max_location = getMaxLocation(lines, len(lines) - 1)
    seeds = getSeeds(lines)
    min_seed = getMinSeed(seeds)

    while current_location <= max_location:
        to_use = [0, 0, 0]
        line, info_map = makeStringIntoList(lines[line_num])
        if ":" in line:
            line_num -= 1
        if " " in line and "map" not in line:
            search, seed_exists, checked, line_num = findNext(search, info_map, to_use, line_num, checked, lines,
                                                               line, seeds_that_dont_exist, seeds, seed_ranges, min_seed)
            if seed_exists and current_location < location:
                location = current_location
                print("found seed:", search)
            if checked == 7 and not seed_exists:
                seeds_that_dont_exist.add(search)
        line_num -= 1

        if line_num < 0:
            line_num = len(lines) - 1
            checked = 0
            print("one seed checked, location:", current_location)

    print("lowest location:", location)

if __name__ == "__main__":
    main()
