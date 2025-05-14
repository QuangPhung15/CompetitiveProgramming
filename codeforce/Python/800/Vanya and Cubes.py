def solve(n):
	res = 0
	curr = 1

	while (curr <= n):
		res += 1
		n -= curr
		curr += res + 1

	return res

n = int(input())
print(solve(n))