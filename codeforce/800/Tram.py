def solve():
	n = int(input())
	res = 0
	curr = 0

	for i in range(n):
		a, b = map(int, input().split())
		curr += b - a

		res = max(res, curr)

	return res

print(solve())