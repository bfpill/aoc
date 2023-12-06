with open("input.txt", "r") as file:

    file = [line for line in file]
    seeds = [int(v) for v in file[0].split(": ")[1].split(" ")]

    sections = [[] for i in range(7)]

    i = 0
    for line in file[3:]:
        if not line.count(":") and line != "\n":
            sections[i].append([int(v) for v in line.split()])

        elif line != "\n":
            i+=1

    sections.reverse()

    mins = []

    for convs in sections[0]:
        mins.append(convs)


    mins_cp = mins[:]
    mins_cp.sort(key=lambda x:x[0])
    mins.reverse()
    print(mins)
    while mins:
        curr_min = mins.pop(0)
        curr_min_start = curr_min[1]
        curr_min_r = curr_min[2]

        out = recursion(curr_min_start, curr_min_r, len(sections)-1)
        if out:
            break

    print(out)
    # for n_seed in seeds:
   # for i in range(0, len(seeds), 2):
   #     for j in range(seeds[i+1]):
   #         n_seed = seeds[i] + j

   #         print(n_seed)
   #         for sec in sections:
   #             for convs in sec:
   #                 dest = convs[0]
   #                 source = convs[1]
   #                 r = convs[2]

   #                 if n_seed >= source and n_seed < source + r:
   #                     n_seed = dest + (n_seed - source)
   #                     print(n_seed)
   #                     break

   #         p2_seeds.append(n_seed)
   #         print("\n")


   # print(min(p2_seeds))




#    new_seeds = []
#    for seed in p2_seeds:
#        for sec in sections[1:]:
#            for convs in sec:
#                r = convs[2]
#                if seed < convs[1] + r and seed >= convs[1]:
#                    #print(seed)
#                    diff = seed - convs[1]
#                    seed = convs[0] + diff
#                    break
#
#        new_seeds.append(seed)
#        print(seed)
#
#    print(min(new_seeds))


