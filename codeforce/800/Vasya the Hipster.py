def solve():
	res = [0, 0]
	a, b = map(int, input().split())

	res[0] = min(a, b)
	res[1] = (a + b) // 2 - res[0]

	return res

print(*solve())