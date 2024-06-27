def solve(n):
	res = []

	if (n % 2 == 1):
		return [-1]

	for i in range(1, n + 1, 2):
		res.append(i + 1)
		res.append(i)

	return res

n = int(input())
print(*solve(n))