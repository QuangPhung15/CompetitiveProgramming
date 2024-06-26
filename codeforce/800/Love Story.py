def solve(s):
	res = 0
	target = "codeforces"

	for i, c in enumerate(s):
		if (c != target[i]):
			res += 1

	return res

t = int(input())
for _ in range(t):
	s = input()
	print(solve(s))