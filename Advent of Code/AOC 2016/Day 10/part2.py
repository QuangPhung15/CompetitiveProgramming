import collections

with open("input.txt") as file:
    data = file.read().splitlines()
    bots, adj = collections.defaultdict(list), collections.defaultdict(list)

    for d in data:
        line = d.split()

        if (line[0] == "value"):
            bots[line[-1]].append(int(line[1]))
        else:
            adj[line[1]].append((line[3], line[5], line[6]))
            adj[line[1]].append((line[8], line[10], line[11]))

res = 1
q = collections.deque()
target_low, target_high = 17, 61

for k, v in bots.items():
    if (len(v) == 2):
        q.append(k)

while (q):
    curr = q.popleft()
    low, high = min(bots[curr][0], bots[curr][1]), max(bots[curr][0], bots[curr][1])

    for value, category, key in adj[curr]:
        if (category == "output" and key in ("0", "1", "2")):
            if (value == "low"):
                res *= low
            else:
                res *= high
        else:
            if (value == "low"):
                bots[key].append(low)
            else:
                bots[key].append(high)
        
            if (len(bots[key]) == 2):
                q.append(key)

print(res)
