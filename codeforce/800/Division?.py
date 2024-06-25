def solve(n):
	if (n >= 1900):
		return "Division 1"
	elif (n >= 1600):
		return "Division 2"
	elif (n >= 1400):
		return "Division 3"
	else:
		return "Division 4"

t = int(input())
for _ in range(t):
	n = int(input())
	print(solve(n))