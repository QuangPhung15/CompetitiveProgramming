with open("input.txt") as file:
    data = file.read().splitlines()
    locations = [[], []]

    for d in data:
        a, b = map(int, d.split())
        locations[0].append(a)
        locations[1].append(b)

res = 0
n = len(locations[0])
locations[0].sort()
locations[1].sort()

for i in range(n):
    res += abs(locations[0][i] - locations[1][i])

print(res)
