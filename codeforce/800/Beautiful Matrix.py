def solve():
	matrix = []

	for i in range(5):
		matrix.append(input().split())

	for i in range(5):
		for j in range(5):
			if (matrix[i][j] == "1"):
				return abs(2 - i) + abs(2 - j)

print(solve())