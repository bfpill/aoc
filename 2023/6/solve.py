import sys


D = open(sys.argv[1]).read().split("\n")
L = [line.split(":") for line in D]

times = [int(x) for x in L[0][1].split()]
dists = [int(x) for x in L[1][1].split()]

n_ways = 1
for i in range(len(times)):
    min_speed = int(dists[i]/times[i])
    max_speed = times[i]

    d_covs = []
    for speed in range(min_speed, max_speed):
        d_cov = speed*(times[i]-speed)

        if d_cov > dists[i]:
            d_covs.append(d_cov)

    n_ways *= len(d_covs)

print(n_ways)
