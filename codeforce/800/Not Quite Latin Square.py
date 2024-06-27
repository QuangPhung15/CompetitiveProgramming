def solve(grid):
	for g in grid:
		if ("?" in g):
			for c in "ABC":
				if (c not in g):
					return c

t = int(input())
for _ in range(t):
	grid = []
	for i in range(3):
		grid.append(input())

	print(solve(grid))