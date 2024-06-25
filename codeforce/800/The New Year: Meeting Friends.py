def solve():
	nums = list(map(int, input().split()))
	nums.sort()

	return nums[1] - nums[0] + nums[2] - nums[1]

print(solve())
