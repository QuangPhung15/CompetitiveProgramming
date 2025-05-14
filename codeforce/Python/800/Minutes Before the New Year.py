def solve(h, m):
	if (m > 0):
		return (23 - h) * 60 + 60 - m

	return (24 - h) * 60

t = int(input())
for _ in range(t):
	h, m = map(int, input().split())
	print(solve(h, m))