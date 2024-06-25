def solve(n):
	res = []
	odd, even = 0, 0

	if (n % 4 != 0):
		return "NO", res

	for i in range(2, n + 1, 2):
		res.append(i)
		even += i

	for i in range(1, n - 2, 2):
		res.append(i)
		odd += i

	res.append(even - odd)
	return "YES", res

t = int(input())
for _ in range(t):
	n = int(input())
	ans, res = solve(n)
	print(ans)
	print(*res)
