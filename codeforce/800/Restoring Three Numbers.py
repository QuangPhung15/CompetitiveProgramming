def solve(nums):
	nums.sort()
	res = [0, 0, 0]

	res[0] = nums[3] - nums[0]
	res[1] = nums[3] - nums[1]
	res[2] = nums[3] - nums[2]

	return res

nums = list(map(int, input().split()))
print(*solve(nums))