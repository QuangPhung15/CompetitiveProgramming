def solve():
	n, k = map(int, input().split())
	nums = list(map(int, input().split()))
	count = 0

	for n in nums:
		if (n + k <= 5):
			count += 1

	return count // 3

print(solve())
