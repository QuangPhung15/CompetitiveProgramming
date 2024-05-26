def solve():
	s = input()
	res = s[0].upper()

	for i in range(1, len(s)):
		res += s[i]

	return res

print(solve())