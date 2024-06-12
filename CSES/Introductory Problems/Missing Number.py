def solve():
	n = int(input())
	nums = list(map(int, input().split()))
	res = (n + 1) * n // 2

	for n in nums:
		res -= n

	return res

print(solve())
