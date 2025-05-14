def solve(n, h, a):
	res = 0

	for p in a:
		if (p > h):
			res += 2
		else:
			res += 1

	return res

n, h = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, h, a))