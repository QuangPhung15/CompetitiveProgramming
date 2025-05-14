def solve(n, p, q):
	res = set()

	for l in p[1::]:
		res.add(l)

	for l in q[1::]:
		res.add(l)

	if (len(res) < n):
		return "Oh, my keyboard!"

	return "I become the guy."

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
print(solve(n, p, q))