def solve(n):
	d, r = n // 3, n % 3

	if (r == 1):
		return [d + 1, d]
	elif (r == 2):
		return [d, d + 1]

	return [d, d]

t = int(input())
for _ in range(t):
	n = int(input())
	print(*solve(n))