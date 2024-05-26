def solve(n):
	res = []
	fact = 1

	while (n > 0):
		if (n % 10 != 0):
			res.append(str(n % 10 * fact))

		n //= 10
		fact *= 10

	print(len(res))
	print(" ".join(res))

t = int(input())
for i in range(t):
	n = int(input())
	solve(n)