def solve():
	n = int(input())
	s = input()
	count = set()

	if (n < 26):
		return "NO"

	for c in s:
		count.add(c.lower())

	if (len(count) == 26):
		return "YES"

	return "NO"

print(solve())