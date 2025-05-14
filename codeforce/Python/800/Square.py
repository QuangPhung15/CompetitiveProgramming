def solve(corners):
	for i in range(1, 4):
		if (corners[0][0] == corners[i][0]):
			return abs(corners[i][1] - corners[0][1]) ** 2

t = int(input())
for _ in range(t):
	corners = []
	for i in range(4):
		x, y = map(int, input().split())
		corners.append([x, y])

	print(solve(corners))