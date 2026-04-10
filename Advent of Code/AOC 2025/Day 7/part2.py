with open("input.txt") as file:
    data = file.read().splitlines()
    manifold = [list(d) for d in data]

res = -1
m, n = len(manifold), len(manifold[0])
dp = [1] * n

for i in reversed(range(m - 1)):
    curr = [0] * n

    for j in range(n):
        if (manifold[i + 1][j] == "^"):
            curr[j] = dp[j - 1] + dp[j + 1]
        else:
            curr[j] = dp[j]
    
    dp = curr.copy()

for j in range(n):
    if (manifold[0][j] == "S"):
        res = dp[j]
        break

print(res)
