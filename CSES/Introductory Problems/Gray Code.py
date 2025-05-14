def solve(n):
	res = []

	for i in range(1 << n):
		curr = i ^ (i >> 1)
		res.append(bin(curr)[2::])

	return res

n = int(input())
print(*solve(n), sep = "\n")