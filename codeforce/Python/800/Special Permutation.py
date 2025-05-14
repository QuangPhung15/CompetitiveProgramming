def solve(n):
	res = [0] * n
	l = 1

	for i in range(1, n + 1):
		res[l % n] = i
		l += 1

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	print(*solve(n))