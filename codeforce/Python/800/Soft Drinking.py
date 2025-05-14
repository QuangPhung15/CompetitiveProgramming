def solve(n, k, l, c, d, p, nl, np):

	return min((k * l) // nl, c * d, p // np) // n

n, k, l, c, d, p, nl, np = map(int, input().split())
print(solve(n, k, l, c, d, p, nl, np))