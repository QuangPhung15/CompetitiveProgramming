def solve(n):
	MOD = 10**9 + 7

	return pow(2, n) % MOD

n = int(input())
print(solve(n))
