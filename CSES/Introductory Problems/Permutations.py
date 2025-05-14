def solve(n):
	res = []

	if (n == 3 or n == 2):
		return "NO SOLUTION"

	for i in range(2, n + 1, 2):
		res.append(i)

	for i in range(1, n + 1, 2):
		res.append(i)

	return res

n = int(input())
res = solve(n)
if (res == "NO SOLUTION"):
	print(res)
else:
	print(*res)
