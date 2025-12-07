with open("input.txt") as file:
    data = file.read()
    instructions = data.split(", ")

r, c = 0, 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
l = 0

for i in instructions:
    d, steps = i[0], int(i[1:])

    if (d == "R"):
        l = (l + 1) % 4
    else:
        l = (l - 1) % 4

    dr, dc = dirs[l]
    r += dr * steps
    c += dc * steps

res = abs(r) + abs(c)

print(res)
