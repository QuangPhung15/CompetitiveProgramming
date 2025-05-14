def solve(k, n, w):
	res = n

	for i in range(w):
		res -= k * (i + 1)

	if (res >= 0):
		return 0

	return abs(res)

k, n, w = map(int, input().split())
print(solve(k, n, w))