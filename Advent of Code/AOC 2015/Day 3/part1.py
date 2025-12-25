with open("input.txt") as file:
    data = file.read()
    directions = data

res = 1
r, c = 0, 0
seen = set([(0, 0)])
dirs = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

for d in directions:
    dr, dc = dirs[d]
    r += dr
    c += dc

    if ((r, c) not in seen):
        res += 1
    
    seen.add((r, c))

print(res)
