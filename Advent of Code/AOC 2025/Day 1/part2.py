with open("input.txt") as file:
    data = file.read().splitlines()
    moves = data

res = 0
curr = 50

for m in moves:
    d, count = m[0], int(m[1:])

    res += count // 100
    count %= 100

    if (d == "L"):
        if (curr > 0 and count >= curr):
            res += 1

        curr = (curr - count) % 100
    else:
        if (count >= 100 - curr):
            res += 1

        curr = (curr + count) % 100

print(res)
