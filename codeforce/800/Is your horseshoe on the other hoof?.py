def solve(nums):
	res = set(nums)

	return 4 - len(res)

nums = map(int, input().split())
print(solve(nums))