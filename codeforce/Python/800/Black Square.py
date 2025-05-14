def solve(nums, s):
	res = 0

	for c in s:
		res += nums[int(c) - 1]

	return res

nums = list(map(int, input().split()))
s = input()
print(solve(nums, s))