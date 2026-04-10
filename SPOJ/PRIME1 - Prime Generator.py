#number-theory
n = int(input())

for _ in range(n):
	a, b = input().split()
	a, b = int(a), int(b)

	prime = [True] * (b + 1)

	p = 2
	while (p**2 <= b):
		if (prime[p] == True):
			for i in range(p * p, b + 1, p):
				prime[i] = False

		p += 1

	for i in range(max(2, a), b + 1):
		if (prime[i] == True):
			print(i)
