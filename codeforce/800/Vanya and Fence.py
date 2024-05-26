def solve():
	n, h = map(int, input().split())
	a = list(map(int, input().split()))
	res = 0

	for p in a:
		if (p > h):
			res += 2
		else:
			res += 1

	return res

print(solve())