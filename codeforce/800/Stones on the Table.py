def solve():
	n = int(input())
	s = input()
	res = 0

	i = 1
	while (i < len(s)):
		while (i < len(s) and s[i] == s[i - 1]):
			res += 1
			i += 1

		i += 1

	return res

print(solve())