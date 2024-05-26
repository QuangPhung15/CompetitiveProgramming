import collections
def solve():
	n, t = map(int, input().split())
	s = list(input())
	q = collections.deque()

	for i in range(len(s)):
		if (s[i] == "B"):
			q.append(i)

	for _ in range(t):
		n = len(q)
		for _ in range(n):
			i = q.popleft()

			if (i < len(s) - 1 and s[i + 1] == "G"):
				s[i], s[i + 1] = s[i + 1], s[i]
				q.append(i + 1)
			elif (i < len(s) - 1 and s[i + 1] == "B"):
				q.append(i)

	return "".join(s)

print(solve())
