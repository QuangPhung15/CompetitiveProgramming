def solve(x):
	if (x % 2 == 0):
		return [x // 2, x // 2]
	else:
		return [x - 1, 1]

t = int(input())
for _ in range(t):
	x = int(input())
	print(*solve(x))