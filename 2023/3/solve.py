import math

with open("input.txt", "r") as file:
    p1 = 0
    p2 = 0
    c_board = [line for line in file]

    def parse_at_pos(x, y):
        if c_board[x][y].isdigit():
            p_l, p_r = y, y

            while p_l > 0 and c_board[x][p_l - 1].isdigit():
                p_l -= 1
            while p_r + 1 < len(c_board[x]) and c_board[x][p_r + 1].isdigit():
                p_r += 1

            num = c_board[x][p_l:p_r+1]
            c_l = list(c_board[x])

            for i in range(p_l, p_r+1):
                c_l[i] = "."

            c_board[x] = ''.join(c_l)

            return int(num)


    for i in range(len(c_board)):
        for j in range(len(c_board[i])-2):
            c = c_board[i][j]
            if not c.isdigit() and not c == ".":
                ns = []
                for f in range(-1, 2):
                    for k in range(-1, 2):
                        if f+i < len(c_board) and k+j < len(c_board[f+i]):
                            o = parse_at_pos(f+i, k+j)
                            if o:
                                ns.append(o)

                print(c, ns)
                if c == "*" and len(ns) == 2:
                    p2 += math.prod(ns)

                p1 += sum(ns)


    print(p1, p2)

