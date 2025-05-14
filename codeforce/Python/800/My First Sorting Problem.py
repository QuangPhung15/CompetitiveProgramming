def solve(x, y):
	return [min(x, y), max(x, y)]

t = int(input())
for _ in range(t):
	x, y = map(int, input().split())
	print(*solve(x, y))