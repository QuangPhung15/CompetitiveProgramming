import collections

with open("input.txt") as file:
    data = file.read().splitlines()
    adj = collections.defaultdict(list)

    for d in data:
        line = d.split()
        adj[line[0]].append((int(line[4]), line[2]))
        adj[line[2]].append((int(line[4]), line[0]))

res = float("-inf")
n = len(adj)
visited = set()

def backtrack(curr, dist):
    global res 

    if (len(visited) == n):
        res = max(res, dist)
        return

    for d, a in adj[curr]:
        if (a in visited):
            continue
            
        visited.add(a)
        backtrack(a, dist + d)
        visited.remove(a)

for k in adj.keys():
    visited.add(k)
    backtrack(k, 0)
    visited.remove(k)

print(res)
