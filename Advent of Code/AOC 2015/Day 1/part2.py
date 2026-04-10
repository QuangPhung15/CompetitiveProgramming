with open("input.txt") as file:
    data = file.read()
    instructions = data

res = 0
floor = 0

for i in instructions:
    res += 1

    if (i == "("):
        floor += 1
    else:
        floor -= 1

    if (floor < 0):
        break

print(res)
