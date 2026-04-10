with open("input.txt") as file:
    data = file.read().splitlines()
    tiles = [list(map(int, d.split(","))) for d in data]

def find_area(cor1, cor2):
    width = abs(cor1[0] - cor2[0]) + 1
    height = abs(cor1[1] - cor2[1]) + 1
    
    return width * height

res = 0
n = len(tiles)

for i in range(n - 1):
    for j in range(i + 1, n):
        res = max(res, find_area(tiles[i], tiles[j]))

print(res)
