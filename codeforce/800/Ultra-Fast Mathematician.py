def solve():
	a, b = input(), input()
	res = ""

	for i in range(len(a)):
		if (a[i] == b[i]):
			res += "0"
		else:
			res += "1"

	return res

print(solve())