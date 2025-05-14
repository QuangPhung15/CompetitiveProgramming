import collections

def solve(s):
	res = ""
	count = collections.defaultdict(int)
	odd = ""

	for c in s:
		count[c] += 1

	for k, v in count.items():
		if (v % 2 == 0):
			res += k * (v // 2)
		else:
			if (odd != ""):
				return "NO SOLUTION"

			odd = k
			res += k * ((v - 1) // 2)

	return res + odd + res[::-1]

s = input()
print(solve(s))