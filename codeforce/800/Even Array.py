def solve(n, nums):
	odd, even = 0, 0

	for i in range(n):
		if (i % 2 != nums[i] % 2):
			if (nums[i] % 2 == 0):
				even += 1
			else:
				odd += 1

	if (odd != even):
		return -1

	return odd

t = int(input())
for _ in range(t):
	n = int(input())
	nums = list(map(int, input().split()))
	print(solve(n, nums))