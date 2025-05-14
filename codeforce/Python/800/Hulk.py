def solve(n):
	res = "I hate "

	for i in range(n - 1):
		res += "that "
		if (i % 2 == 1):
			res += "I hate "
		else:
			res += "I love "

	return res + "it"

n = int(input())
print(solve(n))
