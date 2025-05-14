def solve(n, responses):
	res = 0
	mx = 0

	for i, (a, b) in enumerate(responses):
		if (a <= 10 and b > mx):
			res = i + 1
			mx = b

	return res

t = int(input())
for _ in range(t):
	n = int(input())
	responses = []
	for i in range(n):
		a, b = map(int, input().split())
		responses.append([a, b])

	print(solve(n, responses))
