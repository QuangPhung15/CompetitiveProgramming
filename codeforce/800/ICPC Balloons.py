def solve(n, s):
	res = 0
	seen = set()

	for c in s:
		if (c not in seen):
			res += 1

		seen.add(c)
		res += 1

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	print(solve(n, s))