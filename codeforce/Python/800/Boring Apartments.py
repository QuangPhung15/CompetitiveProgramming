def solve(x):
	res = 1
	digit = 1
	curr = 1

	while (curr != x):
		curr = curr * 10 + digit

		if (curr > 10000):
			digit += 1
			curr = digit

		res += len(str(curr))

	return res

t = int(input())
for _ in range(t):
	x = int(input())
	print(solve(x))