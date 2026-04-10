def solve(n):
	total = (n + 1) * n // 2
	left, right = [], []

	if (total % 2 == 1):
		return "NO", left, right

	if (n % 2 == 0):
		for i in range(1, n // 2 + 1):
			if (i % 2 == 1):
				left.append(i)
				left.append(n)
			else:
				right.append(i)
				right.append(n)

			n -= 1
	else:
		right.append(n)
		n -= 1

		for i in range(1, n // 2 + 1):
			if (i % 2 == 1):
				left.append(i)
				left.append(n)
			else:
				right.append(i)
				right.append(n)

			n -= 1

	return "YES", left, right

n = int(input())
res, left, right = solve(n)
print(res)

if (res == "YES"):
	print(len(left))
	print(*left)
	print(len(right))
	print(*right)