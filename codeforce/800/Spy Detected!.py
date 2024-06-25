def solve(n, nums):
	for i in range(1, n - 1):
		if (nums[i] != nums[i - 1] and nums[i] != nums[i + 1]):
			return i + 1

	if (nums[0] != nums[1]):
		return 1

	if (nums[n - 1] != nums[n - 2]):
		return n

t = int(input())
for _ in range(t):
	n = int(input())
	nums = list(map(int, input().split()))
	print(solve(n, nums))