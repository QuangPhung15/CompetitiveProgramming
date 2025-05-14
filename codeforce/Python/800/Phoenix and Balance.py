def solve(n):
	x, y = 2**n, 0

	for i in range(1, n):
		if (i < n // 2):
			x += 2**i
		else:
			y += 2**i

	return abs(x - y)

t = int(input())
for _ in range(t):
	n =int(input())
	print(solve(n))