with open("input.txt") as file:
    data = file.read().splitlines()
    floor = data

for i, f in enumerate(floor):
    floor[i] = list(f)

res = 0
m, n = len(floor), len(floor[0])

def helper(r, c):
    count = 0

    for dr in range(-1, 2):
        for dc in range(-1, 2):
            newR, newC = r + dr, c + dc

            if (newR < 0 or newR >= m or newC < 0 or newC >= n):
                continue

            if (dr == 0 and dc == 0):
                continue

            if (floor[newR][newC] == "@"):
                count += 1

    return count

is_changed = True

while (is_changed):
    is_changed = False

    for i in range(m):
        for j in range(n):
            if (floor[i][j] == "@"):
                if (helper(i, j) < 4):
                    res += 1
                    floor[i][j] = "."
                    is_changed = True

print(res)
