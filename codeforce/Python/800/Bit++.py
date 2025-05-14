def solve(n, x):
	res = 0

	for i in range(n):
		if (x[i][0] == "+" or x[i][-1] == "+"):
			res += 1
		else:
			res -= 1

n = int(input())
x = []
for i in range(n):
	x.append(input())

print(solve(n, x))