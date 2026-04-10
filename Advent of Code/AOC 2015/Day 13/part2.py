import collections

with open("input.txt") as file:
    data = file.read().splitlines()
    adj = collections.defaultdict(dict)

    for d in data:
        line = d.split()

        if (line[2] == "gain"):
            adj[line[0]][line[-1][:-1]] = int(line[3])
        else:
            adj[line[0]][line[-1][:-1]] = -int(line[3])

res = float("-inf")
visited = set()

def backtrack(curr):
    if (len(visited) == len(adj)):
        return 0

    res = float("-inf")

    for k, v in adj[curr].items():
        if (k in visited):
            continue
            
        visited.add(k)
        res = max(res, v + adj[k][curr] + backtrack(k))
        visited.remove(k)
    
    return res

for k in adj.keys():
    visited.add(k)
    res = max(res, backtrack(k))
    visited.remove(k)

print(res)
