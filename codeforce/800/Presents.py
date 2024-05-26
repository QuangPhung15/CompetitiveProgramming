def solve():
	n = int(input())
	gifts = map(int, input().split())
	res = [""] * n

	for i, g in enumerate(gifts):
		res[g - 1] = str(i + 1)

	return " ".join(res)

print(solve())