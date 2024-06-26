def solve(a, b):
	res = ""

	for i in range(len(a)):
		if (a[i] == b[i]):
			res += "0"
		else:
			res += "1"

	return res

a, b = input(), input()
print(solve(a, b))