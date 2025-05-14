def solve(n, nums):
	ones, twos = nums.count(1), nums.count(2)

	if (ones % 2 == 1):
		return "NO"

	if (twos % 2 == 1 and ones == 0):
		return "NO"

	return "YES"

t = int(input())
for _ in range(t):
	n = int(input())
	nums = list(map(int, input().split()))
	print(solve(n, nums))