def solve():
	s, t = input(), input()

	if (s == t[::-1]):
		return "YES"
	else:
		return "NO"

print(solve())