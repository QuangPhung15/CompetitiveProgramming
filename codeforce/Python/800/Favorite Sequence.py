def solve(n, b):
	res = []
	l, r = 0, n - 1

	while (l <= r):
		res.append(b[l])

		if (l < r):
			res.append(b[r])

		l += 1
		r -= 1

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	b = list(map(int, input().split()))
	print(*solve(n, b))