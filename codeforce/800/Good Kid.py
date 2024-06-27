def solve(n, a):
	res = 1
	mn = float("inf")
	l = 0

	for i, c in enumerate(a):
		if (c < mn):
			mn = c
			l = i

	a[l] = mn + 1

	for c in a:
		res *= c

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))