def solve(c):
	if (c in "codeforces"):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	c = input()
	print(solve(c))