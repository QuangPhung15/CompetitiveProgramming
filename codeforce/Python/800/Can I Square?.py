import math

def solve(n, a):
	area = sum(a)

	if (int(math.sqrt(area))**2 == area):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))