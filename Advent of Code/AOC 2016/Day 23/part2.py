with open("input2.txt") as file:
    data = file.read().splitlines()
    instructions = []

    for d in data:
        line = d.split()
        instructions.append(list(line))

n = len(instructions)
registers = {
    "a": 12
}
i = 0

while (i < n):
    if (instructions[i][0] == "inc"):
        registers[instructions[i][1]] += 1
        i += 1
    elif (instructions[i][0] == "dec"):
        registers[instructions[i][1]] -= 1
        i += 1
    elif (instructions[i][0] == "jnz"):
        if ((not instructions[i][1].isalpha() and int(instructions[i][1]) != 0) or registers[instructions[i][1]] != 0):
            if (not instructions[i][2].isalpha()):
                i += int(instructions[i][2])
            else:
                i += registers[instructions[i][2]]
        else:
            i += 1
    elif (instructions[i][0] == "cpy"):
        if (not instructions[i][2].isalpha()):
            i += 1
        elif (not instructions[i][1].isalpha()):
            registers[instructions[i][2]] = int(instructions[i][1])
            i += 1
        else:
            registers[instructions[i][2]] = registers[instructions[i][1]]
            i += 1
    elif (instructions[i][0] == "tgl"):
        k = registers[instructions[i][1]]

        if (0 <= i + k < n):
            if (instructions[i + k][0] == "inc"):
                instructions[i + k][0] = "dec"
            elif (instructions[i + k][0] == "dec" or instructions[i + k][0] == "tgl"):
                instructions[i + k][0] = "inc"
            elif (instructions[i + k][0] == "jnz"):
                instructions[i + k][0] = "cpy"
            else:
                instructions[i + k][0] = "jnz"
        
        i += 1
    elif (instructions[i][0] == "mul"):
        registers[instructions[i][1]] *= registers[instructions[i][2]]
        i += 1
    else:
        i += 1

res = registers["a"]
print(res)
