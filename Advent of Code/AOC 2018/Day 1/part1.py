with open("input.txt") as file:
    data = file.read().splitlines()
    changes = data

res = 0

for c in changes:
    d, count = c[0], int(c[1:])

    if d == "+":
        res += count
    else:
        res -= count

print(res)
