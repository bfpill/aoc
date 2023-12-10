D = open("input.txt").read().strip().split("\n")

print(D)

class Node():
    def __init__(self, p1, p2, val):
        self.p1 = p1
        self.p2 = p2
        self.val = val


p1 = 0
p2 = 0

for line in D:
    nodes = [Node(0, 0, int(d)) for d in line.split()]
    se_nodes= [(nodes[0].val, nodes[-1].val)]

    while True:
        next_nodes = []

        for i in range(len(nodes)):
            if i+1 < len(nodes):
                n_val = nodes[i+1].val - nodes[i].val
                next_nodes.append(Node(nodes[i], nodes[i+1], n_val))

        if(nodes and all(node.val == 0 for node in nodes)):
            break

        nodes = next_nodes
        se_nodes.append((next_nodes[0].val, next_nodes[-1].val))

    e_n = 0
    st_n = 0

    se_nodes.reverse()
    for s, e in se_nodes:
        e_n += e
        st_n = s - st_n

    p1 += e_n
    p2 += st_n


print(p1, p2)

