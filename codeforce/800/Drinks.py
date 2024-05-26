def solve():
	n = int(input())
	p = map(int, input().split())

	return sum(p) / n

print(solve())