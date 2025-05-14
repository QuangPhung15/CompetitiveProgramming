def solve(n, a):
	res = 0
	mn = min(a)

	for n in a:
		res += n - mn

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))