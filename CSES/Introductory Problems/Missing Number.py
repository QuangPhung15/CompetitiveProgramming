def solve(n, nums):
	res = (n + 1) * n // 2

	for n in nums:
		res -= n

	return res

n = int(input())
nums = list(map(int, input().split()))
print(solve(n, nums))
