def solve():
	k, n, w = map(int, input().split())
	res = n

	for i in range(w):
		res -= k * (i + 1)

	if (res >= 0):
		return 0

	return abs(res)

print(solve())