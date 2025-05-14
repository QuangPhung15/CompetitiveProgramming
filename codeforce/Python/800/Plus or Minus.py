def solve(a, b, c):
	if (a + b == c):
		return "+"

	if (a - b == c):
		return "-"

t = int(input())
for _ in range(t):
	a, b, c = map(int, input().split())
	print(solve(a, b, c))