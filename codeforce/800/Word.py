def solve(s):
	l, u = 0, 0

	for c in s:
		if (c.islower()):
			l += 1
		else:
			u += 1

	if (u > l):
		return s.upper()

	return s.lower()

s = input()
print(solve(s))