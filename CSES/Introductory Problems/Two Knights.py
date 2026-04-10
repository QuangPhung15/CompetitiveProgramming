def solve(n):
	res = []

	for k in range(1, n + 1):
		pairs = k * k * (k * k - 1) // 2
		attack = 4 * (k - 1) * (k - 2)
		res.append(pairs - attack)

	return res

n = int(input())
print(*solve(n), sep = "\n")
