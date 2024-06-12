def solve():
	n = int(input())
	nums = list(map(int, input().split()))
	res = 0
	prev = 0

	for n in nums:
		if (n < prev):
			res += prev - n
		else:
			prev = n

	return res

print(solve())