def solve(n, k, a):
	for x in a:
		if (x == k):
			return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	print(solve(n, k, a))