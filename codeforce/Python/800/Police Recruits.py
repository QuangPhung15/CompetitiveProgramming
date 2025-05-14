def solve(n, nums):
	res = 0
	curr = 0

	for i in range(n):
		if (nums[i] != -1):
			curr += nums[i]
		else:
			if (curr > 0):
				curr -= 1
			else:
				res += 1

	return res

n = int(input())
nums = list(map(int, input().split()))
print(solve(n, nums))