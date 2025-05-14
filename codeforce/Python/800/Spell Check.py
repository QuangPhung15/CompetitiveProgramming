def solve(n, s):
	if (n != 5):
		return "NO"

	seen = set("Timur")

	for c in s:
		if (c not in seen):
			return "NO"

		seen.remove(c)

	return "YES"

t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	print(solve(n, s))