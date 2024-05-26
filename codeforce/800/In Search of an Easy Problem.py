def solve():
	n = int(input())
	a = map(int, input().split())

	for c in a:
		if (c == 1):
			return "HARD"

	return "EASY"

print(solve())