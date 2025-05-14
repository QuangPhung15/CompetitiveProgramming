def solve(a, b, c):
	f, s = a - 1, abs(b - c) + c - 1

	if (f < s):
		return 1
	elif (f > s):
		return 2

	return 3

t = int(input())
for _ in range(t):
	a, b, c = map(int, input().split())
	print(solve(a, b, c))