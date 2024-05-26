def solve():
	x = int(input())
	res = x // 5

	return res if (x % 5 == 0) else res + 1

print(solve())