with open("input.txt") as file:
    data = file.read().splitlines()
    manifold = [list(d) for d in data]

res = 0
m, n = len(manifold), len(manifold[0])

for i in range(m - 1):
    for j in range(n):
        if (manifold[i][j] == "." or manifold[i][j] == "^"):
            continue
        elif (manifold[i][j] == "|" or manifold[i][j] == "S"):
            if (manifold[i + 1][j] == "^"):
                res += 1
                manifold[i + 1][j - 1] = "|"
                manifold[i + 1][j + 1] = "|"
            else:
                manifold[i + 1][j] = "|"

print(res)
