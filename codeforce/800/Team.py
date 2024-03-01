n = int(input())
res = 0

for i in range(n):
    p, v, t = map(int, input().split())
    if (p + v + t > 1):
        res += 1

print(res)