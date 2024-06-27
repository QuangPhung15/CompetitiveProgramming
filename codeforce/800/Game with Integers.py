def solve(n):
	if (n % 3 == 0):
		return "Second"

	return "First"

t = int(input())
for _ in range(t):
	n = int(input())
	print(solve(n))