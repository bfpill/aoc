import sys
import re
import pprint
from collections import defaultdict
pp = pprint.PrettyPrinter(indent=4)


print(sys.argv[1])

D = open("input.txt").read().strip()
parts = D.split('\n\n')
seeds, *others = parts

seeds = [int(v) for v in seeds.split(":")[1].split()]

class Function():
    def __init__(self, S):
        lines = S.split("\n")[1:]
        self.tuples = [[int(x) for x in line.split()] for line in lines]


    def apply_one(self, x: int) -> int:
        pass

    # AFAICT
    # this function takes two ranges and decides whether or not the intersect?
    # if the input range is completey BEFORE the target range we dont change
    # if it is completely after we also dont change

    # the if after[1] > after[0] basically checks if src end is after ed
    # because if the check fails st > end which isnt possible, so it must be
    # src_end
    # then it would be (for after)
    # [st                                     ed)
    #                        [src                src_end]
    # [BEFORE               ][INTER             ][AFTER )

    # (for before)
    # [st        ed)
    #                        [src                src_end]

    # [BEFORE      ]
    #              ]         [INTER
    #              ]AFTER                               [

    # this one will mean inter[1] < inter[0] so we do nothing there
    # basicallty inter breaks, there is no inter, it is backwards
    # and after[1] is also broken, and we dont do anything

    def apply_range(self, R):
        A = []
        for (dest, src, sz) in self.tuples:
          src_end = src+sz
          NR = [] #(73, 93) ->
          while R:
            # [st                                     ed)
            #          [src       src_end]
            # [BEFORE ][INTER            ][AFTER        )
            (st,ed) = R.pop()
            # (src,sz) might cut (st,ed)

            # so basically this is a cheeky way of saying the range is before
            # or the range is after

            before = (st,min(ed,src))
            inter = (max(st, src), min(src_end, ed))
            after = (max(src_end, st), ed)

            if before[1]>before[0]:
              NR.append(before)
            if inter[1]>inter[0]:
              A.append((inter[0]-src+dest, inter[1]-src+dest))
            if after[1]>after[0]:
              NR.append(after)

          R = NR
        return A+R

Fs = [Function(s) for s in others]


P2 = []


pairs = list(zip(seeds[::2], seeds[1::2]))
for st, sz in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R = [(st, st+sz)]
  for f in Fs:
    print(R)
    R = f.apply_range(R)
  #print(len(R))
  P2.append(min(R)[0])

print(min(P2))


