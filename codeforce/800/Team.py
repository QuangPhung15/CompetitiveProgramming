def solve(n, teams):
    res = 0

    for p, v, t in teams:
        if (p + v + t > 1):
            res += 1

    return res

n = int(input())
teams = []
for i in range(n):
    p, v, t = map(int, input().split())
    teams.append([p, v, t])

print(solve(n, teams))