with open("input.txt") as file:
    data = file.read().splitlines()
    nodes = []

    for d in data[2:]:
        line = d.split()
        _, x, y = line[0].split("-")
        nodes.append((int(x[1:]), int(y[1:]), int(line[1][:-1]), int(line[2][:-1]), int(line[3][:-1]), int(line[4][:-1])))

res = 0
n = len(nodes)

for i in range(n - 1):
    u1, a1 = nodes[i][3], nodes[i][4]

    for j in range(i + 1, n):
        u2, a2 = nodes[j][3], nodes[j][4]

        if (u1 > 0 and u1 <= a2):
            res += 1
        
        if (u2 > 0 and u2 <= a1):
            res += 1

print(res)
    