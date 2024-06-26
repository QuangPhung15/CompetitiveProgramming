def solve():
	n = int(input())
	res = 0
	curr = 1

	while (curr <= n):
		res += 1
		n -= curr
		curr += res + 1

	return res

print(solve())