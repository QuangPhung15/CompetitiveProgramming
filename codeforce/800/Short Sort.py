def solve(s):
	count = 0

	for i in range(len(s)):
		if (i != ord(s[i]) - ord("a")):
			count += 1

	if (count == 2 or count == 0):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	s = input()
	print(solve(s))