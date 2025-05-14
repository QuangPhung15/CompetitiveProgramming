def solve(n, nums):
	res = [0, 0]
	l, r = 0, n - 1

	while (l <= r):
		if (l <= r):
			if (nums[l] > nums[r]):
				res[0] += nums[l]
				l += 1
			else:
				res[0] += nums[r]
				r -= 1

		if (l <= r):
			if (nums[l] > nums[r]):
				res[1] += nums[l]
				l += 1
			else:
				res[1] += nums[r]
				r -= 1

	return res

n = int(input())
nums = list(map(int, input().split()))
print(*solve(n, nums))