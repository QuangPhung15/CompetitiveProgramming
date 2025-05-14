def solve(n, x):
	n = max(0, n - 2)
	res = 1 + n // x

	if (n % x > 0):
		res += 1

	return res

t = int(input())
for _ in range(t):
	n, x = map(int, input().split())
	print(solve(n, x))