def solve(n, s):
	x, y = 0, 0

	for c in s:
		if (c == "U"):
			y += 1
		elif (c == "D"):
			y -= 1
		elif (c == "R"):
			x += 1
		else:
			x -= 1

		if (x == 1 and y == 1):
			return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	print(solve(n, s))