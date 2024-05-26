def solve():
	n = int(input())
	res = 0
	prev = ""

	for _ in range(n):
		m = input()
		if (m != prev):
			res += 1

		prev = m

	return res

print(solve())