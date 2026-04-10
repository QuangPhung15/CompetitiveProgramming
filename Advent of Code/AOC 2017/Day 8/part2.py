from collections import defaultdict

with open("input.txt") as file:
    data = file.read().splitlines()
    instructions = [d.split() for d in data]

res = 0
registers = defaultdict(int)

for inst in instructions:
    condition = False

    if (inst[5] == ">" and registers[inst[4]] > int(inst[6])):
        condition = True
    elif (inst[5] == "<" and registers[inst[4]] < int(inst[6])):
        condition = True
    elif (inst[5] == ">=" and registers[inst[4]] >= int(inst[6])):
        condition = True
    elif (inst[5] == "<=" and registers[inst[4]] <= int(inst[6])):
        condition = True
    elif (inst[5] == "==" and registers[inst[4]] == int(inst[6])):
        condition = True
    elif (inst[5] == "!=" and registers[inst[4]] != int(inst[6])):
        condition = True
    
    if (not condition):
        continue

    if (inst[1] == "inc"):
        registers[inst[0]] += int(inst[2])
    else:
        registers[inst[0]] -= int(inst[2])
    
    res = max(res, registers[inst[0]])

print(res)
