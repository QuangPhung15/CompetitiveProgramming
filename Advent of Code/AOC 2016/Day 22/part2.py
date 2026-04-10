from collections import deque

with open("input.txt") as file:
    data = file.read().splitlines()
    nodes = []

    for d in data[2:]:
        line = d.split()
        _, x, y = line[0].split("-")
        nodes.append((int(x[1:]), int(y[1:]), int(line[1][:-1]), int(line[2][:-1]), int(line[3][:-1]), int(line[4][:-1])))

res = -1
m, n = 36, 25
q = deque()
visited = set()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for node in nodes:
    if (node[-1] == 0):
        q.append((0, (node[0], node[1], m - 1, 0)))
        break

while (q):
    steps, (x, y, gx, gy) = q.popleft()

    if (gx == 0 and gy == 0):
        res = steps
        break

    for dx, dy in dirs:
        newX, newY = x + dx, y + dy

        if (newX < 0 or newX >= m or newY < 0 or newY >= n):
            continue
        
        i1, i2 = x * n + y, newX * n + newY

        if (nodes[i1][2] < nodes[i2][3]):
            continue

        if (newX == gx and newY == gy):
            newState = (gx, gy, x, y)
        else:
            newState = (newX, newY, gx, gy)
        
        if (newState in visited):
            continue
        
        q.append((steps + 1, newState))
        visited.add(newState)

print(res)
