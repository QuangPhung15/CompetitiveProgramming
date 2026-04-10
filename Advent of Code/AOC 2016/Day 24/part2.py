from collections import deque, defaultdict

with open("input.txt") as file:
    data = file.read()
    grid = data.splitlines()

res = float("inf")
m, n = len(grid), len(grid[0])
r, c = -1, -1
count = 0
pos = {}
adj = defaultdict(list)
seen = set([0])

for i in range(m):
    for j in range(n):
        if (grid[i][j] == "0"):
            r, c = i, j
            pos[int(grid[i][j])] = (i, j)
        elif (grid[i][j].isdigit()):
            count += 1
            pos[int(grid[i][j])] = (i, j)

def bfs(src, dest):
    start_x, start_y = pos[src]
    target_x, target_y = pos[dest]
    q = deque([(0, start_x, start_y)])
    visited = set([(start_x, start_y)])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while (q):
        steps, x, y = q.popleft()

        if (x == target_x and y == target_y):
            return steps

        for dx, dy in dirs:
            newX, newY = x + dx, y + dy

            if (newX < 0 or newX >= m or newY < 0 or newY >= n):
                continue

            if ((newX, newY) in visited):
                continue

            if (grid[newX][newY] == "#"):
                continue
            
            q.append((steps + 1, newX, newY))
            visited.add((newX, newY))

for i in range(count):
    for j in range(i + 1, count + 1):
        steps = bfs(i, j)
        adj[i].append((steps, j))
        adj[j].append((steps, i))

def backtrack(i, curr):
    global res

    if (len(seen) == count + 1):
        res = min(res, curr + adj[i][0][0])
        return
    
    for dist, a in adj[i]:
        if (a in seen):
            continue

        seen.add(a)
        backtrack(a, curr + dist)
        seen.remove(a)

backtrack(0, 0)
print(res)
