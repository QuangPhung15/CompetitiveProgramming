def solve():
	n = int(input())
	bills = [100, 20, 10, 5, 1]
	res = 0

	for b in bills:
		res += n // b
		n %= b

	return res

print(solve())