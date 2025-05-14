def solve():
	for i in range(n):
		for j in range(m):
			if (photo[i][j] == "C" or photo[i][j] == "M" or photo[i][j] == "Y"):
				return "#Color"

	return "#Black&White"

n, m = map(int, input().split())
photo = []
for i in range(n):
	photo.append(input().split())

print(solve(n, m, photo))