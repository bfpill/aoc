D = open("input.txt").read().strip().split("\n")

moves = D.pop(0)
D.pop(0)

lms = {line[0:3]: (line[7:10], line[12:15]) for line in D}

def p1():
    i = 0
    curr_node = "AAA"
    while not curr_node == "ZZZ":
        dir = int(moves[i%(len(moves))] == "R")
        curr_node = lms[curr_node][dir]
        print(dir, curr_node)
        i+=1


    print(i)


def p2():
    steps =  []
    for line in D:
        if line[2] == "A":
            i = 0
            curr_node = line[0:3]
            while not curr_node[2] == "Z":
                dir = int(moves[i%(len(moves))] == "R")
                curr_node = lms[curr_node][dir]
                print(dir, curr_node)
                i+=1

            print(i)
            steps.append(i)

    from math import gcd
    lcm = 1
    for i in steps:
        lcm = lcm*i//gcd(lcm, i)

    print(lcm)

p2()




