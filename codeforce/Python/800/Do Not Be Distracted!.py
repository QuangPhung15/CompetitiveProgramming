def solve(n, s):
	seen = set()
	i = 0

	while (i < len(s)):
		if (s[i] in seen):
			return "NO"

		seen.add(s[i])
		i += 1

		while (i < len(s) and s[i] == s[i - 1]):
			i += 1

	return "YES"

t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	print(solve(n, s))