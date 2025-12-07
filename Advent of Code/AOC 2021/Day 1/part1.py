with open("input.txt") as file:
    data = file.read()
    depth = list(map(int, data.splitlines()))

res = 0

for i in range(len(depth) - 1):
    if (depth[i + 1] > depth[i]):
        res += 1

print(res)
