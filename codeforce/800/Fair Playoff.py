def solve(nums):
	mx1, mx2 = 0, 0
	l, r = 0, 0

	for i, n in enumerate(nums):
		if (n > mx1):
			mx2 = mx1
			mx1 = n
			r = l
			l = i
		elif (n > mx2):
			mx2 = n
			r = i

	if (l + r == 1 or l + r == 5):
		return "NO"

	return "YES"

t = int(input())
for _ in range(t):
	nums = list(map(int, input().split()))
	print(solve(nums))