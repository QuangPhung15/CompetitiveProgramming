def solve(a, b, c, d):
	res = 0

	if (b > a):
		res += 1

	if (c > a):
		res += 1

	if (d > a):
		res += 1

	return res

t = int(input())
for _ in range(t):
	a, b, c, d = map(int, input().split())
	print(solve(a, b, c, d))