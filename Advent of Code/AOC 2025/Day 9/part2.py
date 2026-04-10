import collections

with open("example.txt") as file:
    data = file.read().splitlines()
    tiles = [list(map(int, d.split(","))) for d in data]

rows = collections.defaultdict(lambda: [float("inf"), float("-inf")])
cols = collections.defaultdict(lambda: [float("inf"), float("-inf")])

for i in range(len(tiles)):
    y1, x1 = tiles[i]
    y2, x2 = tiles[(i + 1) % len(tiles)]

    if (x1 == x2):
        l, r = min(y1, y2), max(y1, y2)
        rows[x1][0] = min(rows[x1][0], l)
        rows[x1][1] = max(rows[x1][1], r)
    else:
        l, r = min(x1, x2), max(x1, x2)
        cols[y1][0] = min(cols[y1][0], l)
        cols[y1][1] = max(cols[y1][1], r)

for x1 in rows.keys():
    for y2, x2 in cols.items():
        if (x2[0] <= x1 <= x2[1]):
            rows[x1][0] = min(rows[x1][0], y2)
            rows[x1][1] = max(rows[x1][1], y2)

for y1 in cols.keys():
    for x2, y2 in rows.items():
        if (y2[0] <= y1 <= y2[1]):
            cols[y1][0] = min(cols[y1][0], x2)
            cols[y1][1] = max(cols[y1][1], x2)

def check_valid_rec(cor1, cor2):
    y1, x1 = cor1
    y2, x2 = cor2
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for x in range(min_x, max_x + 1):
        if (y1 < rows[x][0] or y1 > rows[x][1]):
            return False

        if (y2 < rows[x][0] or y2 > rows[x][1]):
            return False
    
    for y in range(min_y, max_y + 1):
        if (x1 < cols[y][0] or x1 > cols[y][1]):
            return False

        if (x2 < cols[y][0] or x2 > cols[y][1]):
            return False
        
    return True

    # return (
    #     cols[y2][0] <= x1 <= cols[y2][1] and
    #     rows[x2][0] <= y1 <= rows[x2][1] and
    #     cols[y1][0] <= x2 <= cols[y1][1] and
    #     rows[x1][0] <= y2 <= rows[x1][1]
    # )

def find_area(cor1, cor2):
    width = abs(cor1[0] - cor2[0]) + 1
    height = abs(cor1[1] - cor2[1]) + 1
    
    return width * height

res = 0
n = len(tiles)

for i in range(n - 1):
    for j in range(i + 1, n):
        cor1, cor2 = tiles[i], tiles[j]

        if (check_valid_rec(cor1, cor2)):
            res = max(res, find_area(cor1, cor2))

print(res)
