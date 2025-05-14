def solve(n):
	res = []

	if (n % 2 == 1):
		res.append(3)
		n -= 3

	while (n > 0):
		res.append(2)
		n -= 2

	return res

n = int(input())
res = solve(n)
print(len(res))
print(*res)