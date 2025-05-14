def solve(grid):
	res = ""

	for j in range(8):
		for i in range(8):
			if (grid[i][j] != "."):
				res += grid[i][j]

	return res

t = int(input())
for _ in range(t):
	grid = []
	for i in range(8):
		grid.append(input())

	print(solve(grid))
