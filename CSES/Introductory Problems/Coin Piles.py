def solve(a, b):
	if ((2 * a - b) % 3 != 0 or (2 * a - b) < 0 or (2 * b - a) % 3 != 0 or (2 * b - a) < 0):
		return "NO"

	return "YES"

t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	print(solve(a, b))