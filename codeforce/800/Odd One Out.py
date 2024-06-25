def solve(a, b, c):
	return a ^ b ^ c

t = int(input())
for _ in range(t):
	a, b, c = map(int, input().split())
	print(solve(a, b, c))