import collections
def solve():
	n = int(input())
	home, guest = collections.defaultdict(int), collections.defaultdict(int)
	res = 0

	for i in range(n):
		h, a = map(int, input().split())
		home[h] += 1
		guest[a] += 1

	for k, v in home.items():
		res += v * guest[k]

	return res

print(solve())