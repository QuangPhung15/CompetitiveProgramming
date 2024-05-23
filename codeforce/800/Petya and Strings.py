def solve():
	s1, s2 = input().lower(), input().lower()

	for i in range(len(s1)):
		if (s1[i] > s2[i]):
			return 1
		elif (s1[i] < s2[i]):
			return -1

	return 0

print(solve())
