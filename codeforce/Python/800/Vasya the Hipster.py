def solve(a, b):
	res = [0, 0]

	res[0] = min(a, b)
	res[1] = (a + b) // 2 - res[0]

	return res

a, b = map(int, input().split())
print(*solve())