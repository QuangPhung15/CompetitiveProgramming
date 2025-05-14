def solve(n, k):
	for i in range(k):
		if (n % 10 == 0):
			n //= 10
		else:
			n -= 1

	return n

n, k = map(int, input().split())
print(solve(n, k))