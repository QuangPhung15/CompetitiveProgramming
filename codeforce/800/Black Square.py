def solve():
	nums = list(map(int, input().split()))
	s = input()
	res = 0

	for c in s:
		res += nums[int(c) - 1]

	return res

print(solve())