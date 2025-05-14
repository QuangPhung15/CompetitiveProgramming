def solve(s):
	a, b = 0, 0

	for c in s:
		if (c == "A"):
			a += 1
		else:
			b += 1

	if (a > b):
		return "A"

	return "B"

t = int(input())
for _ in range(t):
	s = input()
	print(solve(s))