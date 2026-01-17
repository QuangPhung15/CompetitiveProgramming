from collections import defaultdict

with open("input.txt") as file:
    data = file.read().splitlines()
    weight, adj = {}, defaultdict(list)

    for d in data:
        line = d.split()
        w = int(line[1][1:-1])
        weight[line[0]] = w

        if (len(line) == 2):
            continue

        for i in range(3, len(line)):
            if (line[i][-1] == ","):
                adj[line[0]].append(line[i][:-1])
            else:
                adj[line[0]].append(line[i])

res = ""
chilren = set()

for value in adj.values():
    for v in value:
        chilren.add(v)

for w in weight.keys():
    if (w not in chilren):
        res = w
        break

print(res)
