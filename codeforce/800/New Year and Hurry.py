def solve():
	res = 0
	n, k = map(int, input().split())
	k = 240 - k
	l, r = 1, n

	while (l <= r):
		m = l + (r - l) // 2
		curr = ((m + 1) * m // 2) * 5

		if (curr <= k):
			res = m
			l = m + 1
		else:
			r = m - 1

	return res

print(solve())