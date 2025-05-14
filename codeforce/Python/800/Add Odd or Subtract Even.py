def solve(a, b):
	diff = abs(a - b)

	if (a == b):
		return 0

	if (a > b):
		if (diff % 2 == 0):
			return 1
		else:
			return 2

	if (a < b):
		if (diff % 2 == 1):
			return 1
		else:
			return 2

t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	print(solve(a, b))
