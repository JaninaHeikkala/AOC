f = open("input.txt", "r")

location = 0
seeds = []

information_lists = {}
type_of_thing = ""

going_though_information = False

for line in f:
    line = line.rstrip()

    if not going_though_information:

        if "seeds: " in line:
            line = line.replace("seeds: ", "")
            seeds_str = line.split()
            seeds = [int(num) for num in seeds_str]
            #print(seeds)
        if line == "":
            going_though_information = False
        if "map:" in line:
            line = line.replace(" map:", "")
            type_of_thing = line
            information_lists[line] = {}
            going_though_information = True
    else:
        if line == "":
            going_though_information = False
        else:
            information_str = line.split()
            information_int = [int(num) for num in information_str]
            i = 0
            dic = information_lists[type_of_thing]
            while i < information_int[2]:
                dic[information_int[1]+i] = information_int[0]+i
                #print(information_lists)
                i += 1
            information_lists[type_of_thing] = dic
        

print(information_lists)
    
        

print (location)