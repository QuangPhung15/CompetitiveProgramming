def solve():
	n = int(input())
	primes = [True] * (n + 1)
	p = 2
	l, r = 2, n - 2

	while (p * p <= n):
		if (primes[p] == True):
			for i in range(p * p, n + 1, p):
				primes[i] = False

		p += 1

	while (primes[l] or primes[r]):
		l += 1
		r -= 1

	return [l, r]

print(*solve())
