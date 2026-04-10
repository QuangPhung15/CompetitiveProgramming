with open("input.txt") as file:
    data = file.read().splitlines()
    moves = data

res = 0
curr = 50

for m in moves:
    d, count = m[0], int(m[1:])

    if (d == "L"):
        curr = (curr - count) % 100
    else:
        curr = (curr + count) % 100

    if (curr == 0):
        res += 1

print(res)
