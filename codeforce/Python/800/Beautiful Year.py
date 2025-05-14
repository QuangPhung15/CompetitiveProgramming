def solve(y):
	while (True):
		y += 1
		a, b, c, d = list(str(y))

		if (a != b and a != c and a != d and b != c and b != d and c != d):
			return y

y = int(input())
print(solve(y))