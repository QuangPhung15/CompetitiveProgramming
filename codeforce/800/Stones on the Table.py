def solve(n, s):
	res = 0

	i = 1
	while (i < len(s)):
		while (i < len(s) and s[i] == s[i - 1]):
			res += 1
			i += 1

		i += 1

	return res

n = int(input())
s = input()
print(solve(n, s))