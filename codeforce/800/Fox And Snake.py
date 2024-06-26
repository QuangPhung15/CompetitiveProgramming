def solve(n, m):
	flag = 1

	for i in range(n):
		if (i % 2 == 0):
			print("#" * m)
		else:
			if (flag == 1):
				print("." * (m - 1) + "#")
			else:
				print("#" + "." * (m - 1))

			flag *= -1

n, m = map(int, input().split())
solve(n, m)
