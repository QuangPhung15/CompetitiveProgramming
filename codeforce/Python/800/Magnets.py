def solve(n, magnets):
	res = 0

	for i in range(1, n):
		if (magnets[i] != magnets[i - 1]):
			res += 1

	return res

n = int(input())
magnets = []
for i in range(n):
	m = input()
	magnets.append(m)

print(solve(n, magnets))