def solve(n):
	res = 0

	for _ in range(n):
		s = input()

		if (s == "Tetrahedron"):
			res += 4
		elif (s == "Cube"):
			res += 6
		elif (s == "Octahedron"):
			res += 8
		elif (s == "Dodecahedron"):
			res += 12
		else:
			res += 20

	return res

n = int(input())
print(solve(n))
