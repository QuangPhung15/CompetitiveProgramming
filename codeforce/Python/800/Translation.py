def solve(s, t):
	if (s == t[::-1]):
		return "YES"
	else:
		return "NO"

s, t = input(), input()
print(solve(s, t))