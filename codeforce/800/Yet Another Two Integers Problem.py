def solve(a, b):
	diff = abs(a - b)

	if (diff % 10 > 0):
		return diff // 10 + 1

	return diff // 10

t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	print(solve(a, b))