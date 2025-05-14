def solve(s):
	if (s[0].lower() == "y" and s[1].lower() == "e" and s[2].lower() == "s"):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	s = input()
	print(solve(s))