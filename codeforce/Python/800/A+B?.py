def solve(s):
	a, b = int(s[0]), int(s[2])
	return a + b

t = int(input())
for _ in range(t):
	s = input()
	print(solve(s))