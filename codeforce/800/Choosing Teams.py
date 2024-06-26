def solve(n, k, nums):
	count = 0

	for n in nums:
		if (n + k <= 5):
			count += 1

	return count // 3

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(solve(n, k, nums))
