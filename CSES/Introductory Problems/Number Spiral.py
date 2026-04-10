def solve(y, x):
	if (y > x):
		res = (y - 1) * (y - 1)
		if (y % 2 != 0):
			add = x
		else:
			add = 2 * y - x
	else:
		res = (x - 1) * (x - 1)
		if (x % 2 == 0):
			add = y
		else:
			add = 2 * x - y

	return res + add

t = int(input())
for _ in range(t):
	y, x = map(int, input().split())
	print(solve(y, x))