def solve(s):
	res = 0
	curr = 0

	for c in s:
		i = ord(c) - ord("a")
		diff = abs(i - curr)
		res += min(diff, 26 - diff)
		curr = i

	return res

s = input()
print(solve(s))