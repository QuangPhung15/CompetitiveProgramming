def solve(s):
	curr = 0

	for i in range(3):
		curr += int(s[i])

	for i in range(3, len(s)):
		curr -= int(s[i])

	if (curr == 0):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	s = input()
	print(solve(s))