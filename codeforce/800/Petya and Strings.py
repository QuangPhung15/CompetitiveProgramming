def solve(s1, s2):
	s1, s2 = s1.lower(), s2.lower()

	for i in range(len(s1)):
		if (s1[i] > s2[i]):
			return 1
		elif (s1[i] < s2[i]):
			return -1

	return 0

s1 = input()
s2 = input()
print(solve(s1, s2))
