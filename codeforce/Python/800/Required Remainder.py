def solve(x, y, n):
	d, r = n // x, n % x

	if (y <= r):
		return x * d + y

	return x * (d - 1) + y

t = int(input())
for _ in range(t):
	x, y, n = map(int, input().split())
	print(solve(x, y, n))