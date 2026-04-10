with open("input.txt") as file:
    data = file.read().splitlines()
    operations = []

    for d in data:
        line = d.split()

        if (line[0] == "swap"):
            if (line[1] == "position"):
                operations.append(("sp", int(line[2]), int(line[5])))
            else:
                operations.append(("sl", line[2], line[5]))
        elif (line[0] == "rotate"):
            if (line[1] == "left"):
                operations.append(("rl", int(line[2])))
            elif (line[1] == "right"):
                operations.append(("rr", int(line[2])))
            else:
                operations.append(("rb", line[6]))
        elif (line[0] == "reverse"):
            operations.append(("rev", int(line[2]), int(line[4])))
        else:
            operations.append(("mov", int(line[2]), int(line[5])))

s = list("fbgdceah")
n = len(s)

for o in reversed(operations):
    if (o[0] == "sp"):
        i1, i2 = o[1], o[2]
        s[i1], s[i2] = s[i2], s[i1]
    elif (o[0] == "sl"):
        i1, i2 = s.index(o[1]), s.index(o[2])
        s[i1], s[i2] = s[i2], s[i1]
    elif (o[0] == "rl"):
        i = o[1] % n
        s = s[-i:] + s[:n - i] if (i > 0) else s
    elif (o[0] == "rr"):
        i = o[1] % n
        s = s[i:] + s[:i]
    elif (o[0] == "rb"):
        target = s.index(o[1])

        for i in range(n):
            k = (i + 2) % n if (i >= 4) else (i + 1) % n

            if ((i + k) % n == target):
                s = s[k:] + s[:k]
                break
    elif (o[0] == "rev"):
        l, r = o[1], o[2]

        while (l < r):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    else:
        i1, i2 = o[1], o[2]
        c = s.pop(i2)
        s.insert(i1, c)

res = "".join(s)
print(res)
