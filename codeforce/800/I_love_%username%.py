def solve():
	res = 0
	n = int(input())
	points = list(map(int, input().split()))
	mn, mx = points[0], points[0]

	for i in range(1, n):
		if (points[i] < mn):
			res += 1

		if (points[i] > mx):
			res += 1

		mn = min(mn, points[i])
		mx = max(mx, points[i])

	return res

print(solve())