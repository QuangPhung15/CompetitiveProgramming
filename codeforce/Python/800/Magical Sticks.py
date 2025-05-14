def solve(n):
	return n // 2 + n % 2

t = int(input())
for _ in range(t):
	n = int(input())
	print(solve(n))