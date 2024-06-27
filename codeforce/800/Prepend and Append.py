def solve(n, s):
	l, r = 0, n - 1

	while (l < r):
		if (s[l] != s[r]):
			n -= 2
			l += 1
			r -= 1
		else:
			return n

	return n

t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	print(solve(n, s))