def solve(w, h, n):
	count = 1

	while (w % 2 == 0 or h % 2 == 0):
		if (w % 2 == 0):
			count *= 2
			w //= 2

		if (h % 2 == 0):
			count *= 2
			h //= 2

	if (count >= n):
		return "YES"

	return "NO"

t = int(input())
for _ in range(t):
	w, h, n = map(int, input().split())
	print(solve(w, h, n))