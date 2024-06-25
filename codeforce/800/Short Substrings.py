def solve(s):
	res = s[0]

	for i in range(1, len(s), 2):
		res += s[i]

	return res

t = int(input())
for _ in range(t):
	s = input()
	print(solve(s))