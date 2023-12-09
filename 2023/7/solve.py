D = open("input.txt").read().strip().split("\n")

def classify(hand):
    cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}
    hand = [(int(c) if c.isnumeric() else c) for c in hand]

    vals = [cards[c] for c in hand]

    counts = [hand.count(c) for c in hand if hand.count(c) != 1]

    mores = [count for count in counts if count > 2]
    pairs = [count for count in counts if count == 2]
    pair_count = len(pairs)/2

    if vals.count(1):
        jokers = vals.count(1)
        if mores:
            if mores[0] >= 4:
                return (7, (vals))

                if pair_count:
                    return (5, (vals))

            return (4, (vals))

        if pair_count:
            if pair_count == 2:
                return (5, (vals))
            if pair_count == 1:
                return (4, (vals))

        return (2, (vals))

    if mores:
        if mores[0] >= 4:
            return (mores[0] + 2, (vals))

        if pair_count:
            return (5, (vals))

        return (4, (vals))

    if pair_count:
        return (pair_count + 1, (vals))

    return (1, (vals))


ranking = []

for line in D:
    hand, bid = line.split()
    score, vals = classify(hand)
    ranking.append((score, vals, bid))

ranking.sort()

out = 0
for i, (score, vals, bid) in enumerate(ranking):
    print(i, int(score), vals, bid)
    out += (i+1) * int(bid)

print(out)








