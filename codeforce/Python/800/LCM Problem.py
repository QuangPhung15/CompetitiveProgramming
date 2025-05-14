def solve(l, r):
	if (l * 2 <= r):
		return [l, l * 2]

	return [-1, -1]

t = int(input())
for _ in range(t):
	l, r = map(int, input().split())
	print(*solve(l, r))