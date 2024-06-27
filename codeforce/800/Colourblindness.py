def solve(n, s1, s2):
	for c1, c2 in zip(s1, s2):
		if ((c1 == "R" and c2 != "R") or (c2 == "R" and c1 != "R")):
			return "NO"

	return "YES"

t = int(input())
for _ in range(t):
	n = int(input())
	s1 = input()
	s2 = input()
	print(solve(n, s1, s2))