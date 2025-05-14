def solve(n, nums):
	res = []
	p, m, pe = [], [], []

	for i in range(n):
		if (nums[i] == 1):
			p.append(i + 1)
		elif (nums[i] == 2):
			m.append(i + 1)
		else:
			pe.append(i + 1)

	count = min(len(p), len(m), len(pe))
	for i in range(count):
		res.append([p[i], m[i], pe[i]])

	return count, res

n = int(input())
nums = list(map(int, input().split()))
count, res = solve(n, nums)
print(count)
for r in res:
	print(*r)
