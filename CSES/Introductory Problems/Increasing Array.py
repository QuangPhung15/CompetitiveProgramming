def solve(n, nums):
	res = 0
	prev = 0

	for n in nums:
		if (n < prev):
			res += prev - n
		else:
			prev = n

	return res

n = int(input())
nums = list(map(int, input().split()))
print(solve(n, nums))