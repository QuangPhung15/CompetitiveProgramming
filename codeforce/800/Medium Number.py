def solve(nums):
	nums.sort()

	return nums[1]

t = int(input())
for _ in range(t):
	nums = list(map(int, input().split()))
	print(solve(nums))