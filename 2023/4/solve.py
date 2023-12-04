
with open("input.txt", "r") as file:

    points = 0
    lines = [line.split("|") for line in file]

    scores = []

    for w, y in lines:
        w = w.split(" ")
        y = y.split(" ")

        w = [int(v) for v in w if v]
        y = [int(v) for v in y if v]

        win = []
        for v in w:
            if y.count(v):
                win.append(v)

        sc = 0
        sc2 = 0
        if win:
            sc2 = len(win)
            sc = 1
            for i in range(len(win) -1):
                sc *= 2

        scores.append([sc2,1])

    for i in range(len(scores)):
        print(scores[i])
        for j in range(1, scores[i][0]+1):
            scores[i+j][1] += scores[i][1]


    print(sum([score[1] for score in scores]))









