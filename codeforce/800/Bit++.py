def solve():
	n = int(input())
	res = 0

	for i in range(n):
		x = input()

		if (x[0] == "+" or x[-1] == "+"):
			res += 1
		else:
			res -= 1

print(solve())