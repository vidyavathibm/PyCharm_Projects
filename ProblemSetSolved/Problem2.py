from sys import stdin

S = stdin.readline()
d = {}
for c in S:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

data = [[d[c], c] for c in d.keys()]
print data.sort(key=lambda e: [-e[0], e[1]])

for x in range(3):
    print data[x][1], data[x][0]
