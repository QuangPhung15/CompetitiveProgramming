with open("input.txt") as file:
    data = file.read().splitlines()
    instructions = []

    for d in data:
        line = d.split()
        instructions.append(tuple(line))

n = len(instructions)
registers = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
}
i = 0

while (i < n):
    if (instructions[i][0] == "inc"):
        registers[instructions[i][1]] += 1
        i += 1
    elif (instructions[i][0] == "dec"):
        registers[instructions[i][1]] -= 1
        i += 1
    elif (instructions[i][0] == "cpy"):
        if (instructions[i][1].isdigit()):
            registers[instructions[i][2]] = int(instructions[i][1])
        else:
            registers[instructions[i][2]] = registers[instructions[i][1]]
        
        i += 1
    else:
        if ((instructions[i][1].isdigit() and int(instructions[i][1]) != 0) or registers[instructions[i][1]] != 0):
            i += int(instructions[i][2])
        else:
            i += 1

res = registers["a"]
print(res)
