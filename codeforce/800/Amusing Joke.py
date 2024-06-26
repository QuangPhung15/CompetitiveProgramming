def solve(s1, s2, s3):
	count = [0] * 26

	for c in s1:
		count[ord(c) - ord("A")] += 1

	for c in s2:
		count[ord(c) - ord("A")] += 1

	for c in s3:
		count[ord(c) - ord("A")] -= 1

	for i in range(26):
		if (count[i] != 0):
			return "NO"

	return "YES"

s1, s2, s3 = input(), input(), input()
print(solve(s1, s2, s3))