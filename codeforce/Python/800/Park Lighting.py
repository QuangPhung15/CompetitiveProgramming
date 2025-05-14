def solve(n, m):
	cells = n * m
	return cells // 2 + cells % 2

t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	print(solve(n, m))