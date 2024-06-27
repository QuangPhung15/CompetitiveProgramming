def solve(n, s):
	l, r = 0, n - 1

	for i in range(n):
		if (s[i] == "B"):
			l = i
			break

	for i in range(n - 1, -1, -1):
		if (s[i] == "B"):
			r = i
			break

	return r - l + 1

t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	print(solve(n, s))