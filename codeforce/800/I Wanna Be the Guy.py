def solve():
	n = int(input())
	p = list(map(int, input().split()))
	q = list(map(int, input().split()))
	res = set()

	for l in p[1::]:
		res.add(l)

	for l in q[1::]:
		res.add(l)

	if (len(res) < n):
		return "Oh, my keyboard!"

	return "I become the guy."

print(solve())