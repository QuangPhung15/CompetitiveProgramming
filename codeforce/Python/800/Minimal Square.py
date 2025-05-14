def solve(a, b):
	return max((2 * min(a, b)) ** 2, max(a, b) ** 2)

t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	print(solve(a, b))