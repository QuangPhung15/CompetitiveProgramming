def solve(n, a):
	seen = set()

	for c in a:
		if (c in seen):
			return "NO"

		seen.add(c)

	return "YES"

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))