def solve():
	n = int(input())
	s = input()
	d, a = 0, 0

	for i in range(n):
		if (s[i] == "A"):
			a += 1
		else:
			d += 1

	if (a == d):
		return "Friendship"
	elif (a > d):
		return "Anton"
	else:
		return "Danik"

print(solve())