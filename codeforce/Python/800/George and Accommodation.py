def solve(n):
	res = 0

	for i in range(n):
		p, q = map(int, input().split())

		if (q - p >= 2):
			res += 1

	return res

n = int(input())
print(solve())