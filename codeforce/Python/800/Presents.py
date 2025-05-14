def solve(n, gifts):
	res = [""] * n

	for i, g in enumerate(gifts):
		res[g - 1] = str(i + 1)

	return " ".join(res)

n = int(input())
gifts = map(int, input().split())
print(solve(n, gifts))