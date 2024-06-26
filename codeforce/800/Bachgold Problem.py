def solve():
	n = int(input())
	res = []

	if (n % 2 == 1):
		res.append(3)
		n -= 3

	while (n > 0):
		res.append(2)
		n -= 2

	return res

res = solve()
print(len(res))
print(*res)