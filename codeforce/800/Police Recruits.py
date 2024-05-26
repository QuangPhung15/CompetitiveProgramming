def solve():
	n = int(input())
	nums = list(map(int, input().split()))
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

print(solve())

