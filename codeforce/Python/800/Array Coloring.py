def solve(n, a):
	odd, even = 0, 0

	for x in a:
		if (x % 2 == 1):
			odd += 1
		else:
			even += 1

	if (odd % 2 == 1):
		return "NO"

	return "YES"

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))