def solve():
	n, m = map(int, input().split())
	primes = [True] * 51
	p = 2

	while (p * p <= 50):
		if (primes[p]):
			for i in range(p * p, 51, p):
				primes[i] = False

		p += 1

	if (not primes[m]):
		return "NO"

	for i in range(n + 1, m):
		if (primes[i]):
			return "NO"

	return "YES"

print(solve())