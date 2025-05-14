def solve(a, b, c, n):
	mx = max(a, b, c)
	n = n - (mx - a) - (mx - b) - (mx - c)

	if (n < 0 or n % 3 != 0):
		return "NO"

	return "YES"

t = int(input())
for _ in range(t):
	a, b, c, n = map(int, input().split())
	print(solve(a, b, c, n))