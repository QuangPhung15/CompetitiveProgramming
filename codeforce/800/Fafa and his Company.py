def solve(n):
	res = 0
	l, e = 1, n - 1

	while (l <= e):
		if (e % l == 0):
			res += 1

		l += 1
		e -= 1

	return res

n = int(input())
print(solve(n))