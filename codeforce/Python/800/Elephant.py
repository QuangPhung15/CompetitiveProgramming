def solve(x):
	res = x // 5

	return res if (x % 5 == 0) else res + 1

x = int(input())
print(solve(x))