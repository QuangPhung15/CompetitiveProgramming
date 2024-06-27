def solve(n, s):
	res = 0

	for c in s:
		res = max(res, ord(c) - ord("a") + 1)

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	print(solve(n, s))