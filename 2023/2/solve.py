import math

with open('input.txt', 'r') as file:

    max_r = 12
    max_g = 13
    max_b = 14

    sum = 0
    for line in file:
        tks = line.split()

        id = int(tks[1])
        tks.pop(0)
        tks.pop(0)
        bad = False

        min_r = -math.inf
        min_g = -math.inf
        min_b = -math.inf


        for i in range(len(tks)-1, -1, -2):
            color = tks[i]
            count = int(tks[i-1])

            print(color, count)
            if color == "green" and min_g < count:
                min_g = count
            elif color == "blue" and min_b < count:
                min_b = count
            elif color == "red" and min_r < count:
                min_r = count


        print( min_r , min_g , min_b )
        sum += min_r * min_g * min_b

        print("\n")

    print(sum)


