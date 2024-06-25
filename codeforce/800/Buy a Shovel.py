def solve():
	res = 1
	k, r = map(int, input().split())

	while ((k * res) % 10 != 0 and (k * res) % 10 != r):
		res += 1

	return res

print(solve())