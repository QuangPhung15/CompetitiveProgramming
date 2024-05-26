def solve():
	nums = list(map(int, input().split("+")))
	bucket = [0] * 4

	for n in nums:
		bucket[n] += 1

	j = 1
	for i in range(len(nums)):
		while (bucket[j] == 0):
			j += 1

		nums[i] = str(j)
		bucket[j] -= 1

	return "+".join(nums)

print(solve())