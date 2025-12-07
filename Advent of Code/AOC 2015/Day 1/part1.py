with open("input.txt") as file:
    data = file.read()
    instructions = data

res = 0

for i in instructions:
    if (i == "("):
        res += 1
    else:
        res -= 1

print(res)
