def solve(a, b):
	if (a % b == 0):
		return 0

	return b - a % b

t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	print(solve(a, b))