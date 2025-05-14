def solve(s):
	n = len(s)

	if (n % 2 == 1):
		return "NO"

	if (s[:n//2] == s[n//2:]):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	s = input()
	print(solve(s))