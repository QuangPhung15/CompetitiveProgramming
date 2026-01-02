with open("input.txt") as file:
    data = file.read().splitlines()
    triangles = [tuple(map(int, d.split())) for d in data]

res = 0
n = len(triangles)

for i in range(0, n, 3):
    for j in range(3):
        a, b, c = triangles[i][j], triangles[i + 1][j], triangles[i + 2][j]

        longest = max(a, b, c)
        remaining = a + b + c - longest

        if (remaining > longest):
            res += 1

print(res)
