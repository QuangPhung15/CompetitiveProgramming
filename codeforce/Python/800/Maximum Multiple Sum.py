import math

def solve(n):
	res = -1
	mx = 0

	for x in range(2, n + 1):
		f = n // x
		count = ((f + 1) * f // 2) * x

		if (count > mx):
			res = x
			mx = count

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	print(solve(n))