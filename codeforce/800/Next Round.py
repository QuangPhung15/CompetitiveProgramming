def solve(n, k, a):
    res = 0

    for s in a:
        if (s > 0 and s >= a[k - 1]):
            res += 1
        else:
            break

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))