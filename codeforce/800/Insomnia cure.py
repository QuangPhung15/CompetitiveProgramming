def solve(k, l, m, n, d):
	res = 0

	for i in range(1, d + 1):
		if (i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0):
			res += 1

	return res

k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input())
print(solve(k, l, m, n, d))