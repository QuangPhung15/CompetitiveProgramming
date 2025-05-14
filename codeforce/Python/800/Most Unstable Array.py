def solve(n, m):
	if (n == 1):
		return 0

	if (n == 2):
		return m

	return 2 * m

t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	print(solve(n, m))