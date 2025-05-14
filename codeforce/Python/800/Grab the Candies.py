def solve(n, a):
	odd, even = 0, 0

	for x in a:
		if (x % 2 == 1):
			odd += x
		else:
			even += x

	if (even > odd):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))