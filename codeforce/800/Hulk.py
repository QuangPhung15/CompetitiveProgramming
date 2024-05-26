def solve():
	n = int(input())
	res = "I hate "

	for i in range(n - 1):
		res += "that "
		if (i % 2 == 1):
			res += "I hate "
		else:
			res += "I love "

	return res + "it"

print(solve())
