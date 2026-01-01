with open("input.txt") as file:
    data = file.read().splitlines()
    instructions = []

    for d in data:
        line = d.split()

        if (line[0] in ("hlf", "tpl", "inc")):
            instructions.append((line[0], line[1]))
        elif (line[0] == "jmp"):
            instructions.append((line[0], int(line[1])))
        else:
            instructions.append((line[0], line[1][:-1], int(line[2])))

registers = {
    "a": 1,
    "b": 0
}
n = len(instructions)
i = 0

while (i < n):
    if (instructions[i][0] == "hlf"):
        registers[instructions[i][1]] //= 2
        i += 1
    elif (instructions[i][0] == "tpl"):
        registers[instructions[i][1]] *= 3
        i += 1
    elif (instructions[i][0] == "inc"):
        registers[instructions[i][1]] += 1
        i += 1
    elif (instructions[i][0] == "jmp"):
        i += instructions[i][1]
    elif (instructions[i][0] == "jie"):
        if (registers[instructions[i][1]] % 2 == 0):
            i += instructions[i][2]
        else:
            i += 1
    else:
        if (registers[instructions[i][1]] == 1):
            i += instructions[i][2]
        else:
            i += 1

res = registers["b"]
print(res)
