def solve(n, a):
	res = 0
	curr = 0

	for x in a:
		if (x == 0):
			curr += 1
		else:
			curr = 0

		res = max(res, curr)

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))