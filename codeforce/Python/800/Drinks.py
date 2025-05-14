def solve(n, p):
	return sum(p) / n

n = int(input())
p = map(int, input().split())
print(solve(n, p))