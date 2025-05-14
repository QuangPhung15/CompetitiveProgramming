def solve(a, b, c):
	if (a < b < c):
		return "STAIR"

	if (a < b and c < b):
		return "PEAK"

	return "NONE"

t = int(input())
for _ in range(t):
	a, b, c = map(int, input().split())
	print(solve(a, b, c))