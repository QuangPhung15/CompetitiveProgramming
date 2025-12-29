with open("input.txt") as file:
    data = file.read()
    grid = list(map(list, data.splitlines()))

res = 0
m, n = len(grid), len(grid[0])
grid[0][0] = "#"
grid[0][n - 1] = "#"
grid[m - 1][0] = "#"
grid[m - 1][n - 1] = "#"

def helper(r, c):
    count = 0

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            newR, newC = r + dr, c + dc

            if (newR == r and newC == c):
                continue

            if (newR < 0 or newR >= m or newC < 0 or newC >= n):
                continue

            if (grid[newR][newC] == "#"):
                count += 1
    
    return count

for _ in range(100):
    new_grid = [[""] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            count = helper(r, c)

            if (r in (0, m - 1) and c in (0, n - 1)):
                new_grid[r][c] = "#"
            elif (grid[r][c] == "#" and count != 3 and count != 2):
                new_grid[r][c] = "."
            elif (grid[r][c] == "." and count == 3):
                new_grid[r][c] = "#"
            else:
                new_grid[r][c] = grid[r][c]
    
    grid = new_grid.copy()

for r in range(m):
    for c in range(n):
        if (grid[r][c] == "#"):
            res += 1
    
print(res)
