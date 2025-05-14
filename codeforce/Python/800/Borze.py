def solve(s):
	res = ""
	i = 0

	while (i < len(s)):
		if (s[i] == "."):
			res += "0"
		else:
			if (s[i + 1] == "."):
				res += "1"
			else:
				res += "2"

			i += 1

		i += 1

	return res

s = input()
print(solve(s))