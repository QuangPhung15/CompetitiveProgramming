def solve(n):
	lucky = 0

	for c in n:
		if (c == "4" or c == "7"):
			lucky += 1

	for c in str(lucky):
		if (c != "4" and c != "7"):
			return "NO"

	return "YES"

n = input()
print(solve(n))