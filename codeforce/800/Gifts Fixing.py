def solve(n, a, b):
	res = 0
	mn1, mn2 = min(a), min(b)

	for x, y in zip(a, b):
		res += max(x - mn1, y - mn2)

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	print(solve(n, a, b))