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

visited = set(["Alice"])

def backtrack(curr):
    if (len(visited) == len(adj)):
        return adj[curr]["Alice"] + adj["Alice"][curr]

    res = float("-inf")

    for k, v in adj[curr].items():
        if (k in visited):
            continue
            
        visited.add(k)
        res = max(res, v + adj[k][curr] + backtrack(k))
        visited.remove(k)
    
    return res

res = backtrack("Alice")
print(res)
