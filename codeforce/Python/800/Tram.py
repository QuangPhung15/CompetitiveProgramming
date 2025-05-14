def solve(n, trams):

	res = 0
	curr = 0

	for a, b in trams:
		curr += b - a
		res = max(res, curr)

	return res

n = int(input())
trams = []
for i in range(n):
	a, b = map(int, input().split())
	trams.append([a, b])

print(solve(n, trams))