def solve():
	res = 0
	a, b = map(int, input().split())

	while (a <= b):
		res += 1
		a *= 3
		b *= 2

	return res

print(solve())