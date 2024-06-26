def solve(a, b):
	res = 0

	while (a <= b):
		res += 1
		a *= 3
		b *= 2

	return res

a, b = map(int, input().split())
print(solve(a, b))