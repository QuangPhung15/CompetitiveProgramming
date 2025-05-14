def solve(n, a):
	a.sort()

	for i in range(n - 1):
		if (a[i + 1] - a[i] > 1):
			return "NO"

	return "YES"

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))