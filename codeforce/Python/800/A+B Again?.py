def solve(n):
	return n % 10 + n // 10

t = int(input())
for _ in range(t):
	n = int(input())
	print(solve(n))