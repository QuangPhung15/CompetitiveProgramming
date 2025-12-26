with open("input.txt") as file:
    data = file.read().splitlines()
    instructions = {}

    for d in data:
        line = d.split()

        if (len(line) == 3):
            instructions[line[2]] = ("ASSIGN", line[0])
        elif (len(line) == 4):
            instructions[line[3]] = ("NOT", line[1])
        else:
            if (line[1] == "AND"):
                instructions[line[4]] = ("AND", line[0], line[2])
            elif (line[1] == "OR"):
                instructions[line[4]] = ("OR", line[0], line[2])
            elif (line[1] == "LSHIFT"):
                instructions[line[4]] = ("LSHIFT", line[0], int(line[2]))
            else:
                instructions[line[4]] = ("RSHIFT", line[0], int(line[2]))

cache = {}

def dfs(wire):
    if (wire.isdigit()):
        return int(wire)
    
    if (wire not in cache):
        res = None
        i = instructions[wire]

        if (i[0] == "ASSIGN"):
            res = dfs(i[1])
        elif (i[0] == "NOT"):
            res = ~dfs(i[1]) & 65535
        elif (i[0] == "AND"):
            res = dfs(i[1]) & dfs(i[2])
        elif (i[0] == "OR"):
            res = dfs(i[1]) | dfs(i[2])
        elif (i[0] == "LSHIFT"):
            res = dfs(i[1]) << i[2]
        else:
            res = dfs(i[1]) >> i[2]
        
        cache[wire] = res

    return cache[wire]
        
res = dfs("a")
print(res)
