def solve(n, a):
	for c in a:
		if (c == 1):
			return "HARD"

	return "EASY"

n = int(input())
a = map(int, input().split())
print(solve(n, a))