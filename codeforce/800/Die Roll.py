def solve():
	y, w = map(int, input().split())
	chances = 6 - max(y, w) + 1
	common = 1

	for i in range(1, chances + 1):
		if (6 % i == 0 and chances % i == 0):
			common = i

	return f"{chances // common}/{6 // common}"

print(solve())