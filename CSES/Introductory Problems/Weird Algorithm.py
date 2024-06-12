def solve():
	n = int(input())
	nums = []

	while (n != 1):
		nums.append(n)
		if (n % 2 == 0):
			n //= 2
		else:
			n = n * 3 + 1

	nums.append(1)
	return nums

print(*solve())