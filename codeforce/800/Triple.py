import collections

def solve(n, a):
	count = collections.defaultdict(int)

	for x in a:
		count[x] += 1

		if (count[x] == 3):
			return x

	return -1

t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	print(solve(n, a))