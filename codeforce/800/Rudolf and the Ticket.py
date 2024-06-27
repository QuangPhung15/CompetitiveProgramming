def solve(n, m, k, b, c):
	res = 0

	for i in range(n):
		for j in range(m):
			if (b[i] + c[j] <= k):
				res += 1

	return res

t = int(input())
for _ in range(t):
	n, m, k = map(int, input().split())
	b = list(map(int, input().split()))
	c = list(map(int, input().split()))
	print(solve(n, m, k, b, c))