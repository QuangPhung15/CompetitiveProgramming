def solve():
	n = int(input())
	heights = list(map(int, input().split()))
	mx, mn = heights[0], heights[-1]
	l, r = 0, n - 1

	for i in range(n):
		if (heights[i] <= mn):
			r = i
			mn = heights[i]

		if (heights[i] > mx):
			l = i
			mx = heights[i]

	res = n - 1 - r + l
	if (r < l):
		return res - 1

	return res

print(solve())