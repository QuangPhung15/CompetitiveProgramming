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

def dfs(root):
    global res

    if (root not in adj):
        return weight[root]
    
    blocks = []

    for a in adj[root]:
        curr = dfs(a)
        blocks.append([a, curr])
    
    n = len(blocks)

    for i in range(n):
        if (blocks[i][1] != blocks[(i - 1) % n][1] and blocks[i][1] != blocks[(i + 1) % n][1]):
            diff = blocks[(i - 1) % n][1] - blocks[i][1]
            weight[blocks[i][0]] += diff
            res = weight[blocks[i][0]]
            blocks[i][1] = blocks[(i - 1) % n][1]
            break

    return weight[root] + blocks[0][1] * n
    
res = -1
root = ""
chilren = set()

for value in adj.values():
    for v in value:
        chilren.add(v)

for w in weight.keys():
    if (w not in chilren):
        root = w
        break

dfs(root)
print(res)
