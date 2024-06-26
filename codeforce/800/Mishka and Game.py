def solve(n, games):
	m, c = 0, 0

	for a, b in games:
		if (a > b):
			m += 1
		elif (b > a):
			c += 1

	if (m > c):
		return "Mishka"
	elif (m < c):
		return "Chris"

	return "Friendship is magic!^^"

n = int(input())
games = []
for i in range(n):
	a, b = map(int, input().split())
	games.append([a, b])

print(solve(n, games))