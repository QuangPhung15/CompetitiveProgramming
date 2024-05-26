def solve():
	res = set(map(int, input().split()))

	return 4 - len(res)

print(solve())