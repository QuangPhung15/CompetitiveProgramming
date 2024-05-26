def solve():
	s = input()
	char = set()

	for c in s:
		char.add(c)

	if (len(char) % 2 == 1):
		return "IGNORE HIM!"
	else:
		return "CHAT WITH HER!"

print(solve())