def solve(n):
	res = 0

	for i in range(1, 10):
		curr = i

		while (curr <= n):
			res += 1
			curr = curr * 10 + i

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	print(solve(n))