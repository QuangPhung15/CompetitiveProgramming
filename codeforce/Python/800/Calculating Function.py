def solve(n):
	total = (n + 1) * n // 2

	if (n % 2 == 1):
		odd = (n + 1) * (n // 2 + 1) // 2
	else:
		odd = (n - 1 + 1) * (n // 2) // 2

	return total - 2 * odd

n = int(input())
print(solve(n))