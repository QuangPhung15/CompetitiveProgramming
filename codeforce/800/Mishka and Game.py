def solve():
	n = int(input())
	m, c = 0, 0

	for _ in range(n):
		a, b = map(int, input().split())

		if (a > b):
			m += 1
		elif (b > a):
			c += 1

	if (m > c):
		return "Mishka"
	elif (m < c):
		return "Chris"

	return "Friendship is magic!^^"

print(solve())