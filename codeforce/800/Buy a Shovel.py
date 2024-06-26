def solve(k, r):
	res = 1

	while ((k * res) % 10 != 0 and (k * res) % 10 != r):
		res += 1

	return res

k, r = map(int, input().split())
print(solve(k, r))