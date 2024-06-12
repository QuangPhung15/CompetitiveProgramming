def solve():
	s = input()
	res = 0
	l, curr = 0, 0

	for r, c in enumerate(s):
		curr += 1
		while (l <= r and c != s[l]):
			l += 1
			curr -= 1

		res = max(res, curr)

	return res

print(solve())