def solve(n, a):
	res = 1
	curr = 1

	for i in range(1, n):
		if (a[i] > a[i - 1]):
			curr += 1
		else:
			curr = 1

		res = max(res, curr)

	return res

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))