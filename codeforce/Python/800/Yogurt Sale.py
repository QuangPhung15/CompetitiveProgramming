def solve(n, a, b):
	if (a * 2 < b):
		return a * n

	d, r = n // 2, n % 2
	return d * b + a * r

t = int(input())
for _ in range(t):
	n, a, b = map(int, input().split())
	print(solve(n, a, b))