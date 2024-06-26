def solve(nums):
	nums.sort()

	return nums[1] - nums[0] + nums[2] - nums[1]

nums = list(map(int, input().split()))
print(solve(nums))
