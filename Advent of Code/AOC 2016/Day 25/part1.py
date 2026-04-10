with open("input.txt") as file:
    data = file.read().splitlines()
    instructions = [d.split() for d in data]

def solve(a_start):
    n = len(instructions)
    registers = {
        "a": a_start,
        "b": 0,
        "c": 0,
        "d": 0        
    }
    i = 0
    count = 0
    prev = None

    while (0 <= i < n and count < 30):
        inst = instructions[i]

        if (inst[0] == "inc"):
            registers[inst[1]] += 1
            i += 1
        elif (inst[0] == "dec"):
            registers[inst[1]] -= 1
            i += 1
        elif (inst[0] == "cpy"):
            if (inst[1] in registers):
                registers[inst[2]] = registers[inst[1]]
            else:
                registers[inst[2]] = int(inst[1])
            
            i += 1
        elif (inst[0] == "jnz"):
            if ((inst[1] in registers and registers[inst[1]] != 0) or (inst[1] not in registers and int(inst[1]) != 0)):
                i += int(inst[2])
            else:
                i += 1
        else:
            v = registers[inst[1]]

            if (v not in (0, 1)):
                return False
            elif (prev is not None and v == prev):
                return False

            count += 1
            prev = v
            i += 1
        
    return count == 30
            
res = 0

while (True):
    if (solve(res)):
        break

    res += 1

print(res)
