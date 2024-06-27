def solve(a, b):
	res = ["", ""]

	for i in range(3):
		if (i == 0):
			res[0] += b[i]
			res[1] += a[i]
		else:
			res[0] += a[i]
			res[1] += b[i]

	return res

t = int(input())
for _ in range(t):
	a, b = input().split()
	print(*solve(a, b))