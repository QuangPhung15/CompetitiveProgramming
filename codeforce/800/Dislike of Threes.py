def solve(k):
	res = 0

	for i in range(k):
		res += 1

		while (res % 3 == 0 or res % 10 == 3):
			res += 1

	return res

t = int(input())
for _ in range(t):
	k = int(input())
	print(solve(k))