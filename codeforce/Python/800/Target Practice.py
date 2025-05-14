def solve(rings):
	res = 0

	for i in range(10):
		for j in range(10):
			if (rings[i][j] == "X"):
				res += min(i + 1, 10 - i, j + 1, 10 - j)

	return res

t = int(input())
for _ in range(t):
	rings = []
	for _ in range(10):
		rings.append(input())

	print(solve(rings))