def solve(s):
	seen = set()

	for i in range(1, len(s) - 1, 3):
		seen.add(s[i])

	return len(seen)

s = input()
print(solve(s))