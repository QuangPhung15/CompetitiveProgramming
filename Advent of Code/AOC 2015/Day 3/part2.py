with open("input.txt") as file:
    data = file.read()
    directions = data

res = 1
r, c = 0, 0
x, y = 0, 0
seen = set([(0, 0)])
dirs = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

for i in range(0, len(directions), 2):
    dr, dc = dirs[directions[i]]
    dx, dy = dirs[directions[i + 1]]

    r += dr
    c += dc

    if ((r, c) not in seen):
        res += 1
    
    seen.add((r, c))

    x += dx
    y += dy

    if ((x, y) not in seen):
        res += 1
    
    seen.add((x, y))

print(res)
    