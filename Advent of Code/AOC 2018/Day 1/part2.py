with open("input.txt") as file:
    data = file.read().splitlines()
    changes = data

res = 0
visited = set([0])
flag = False

while (not flag):
    for c in changes:
        d, count = c[0], int(c[1:])

        if d == "+":
            res += count
        else:
            res -= count

        if (res in visited):
            flag = True
            break

        visited.add(res)

print(res)
