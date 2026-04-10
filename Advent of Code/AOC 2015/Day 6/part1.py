with open("input.txt") as file:
    data = file.read().splitlines()
    instructions = []

    for d in data:
        line = d.split()

        if (line[0] == "turn" and line[1] == "on"):
            instructions.append((0, tuple(map(int, line[2].split(","))), tuple(map(int, line[4].split(",")))))
        elif (line[0] == "turn" and line[1] == "off"):
            instructions.append((1, tuple(map(int, line[2].split(","))), tuple(map(int, line[4].split(",")))))
        else:
            instructions.append((2, tuple(map(int, line[1].split(","))), tuple(map(int, line[3].split(",")))))

res = 0
grid = [[0] * 1000 for _ in range(1000)]

for c, (x1, y1), (x2, y2) in instructions:
    if (c == 0):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (grid[i][j] == 0):
                    res += 1

                grid[i][j] = 1
    elif (c == 1):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (grid[i][j] == 1):
                    res -= 1

                grid[i][j] = 0
    else:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if (grid[i][j] == 0):
                    res += 1
                    grid[i][j] = 1
                else:
                    res -= 1
                    grid[i][j] = 0

print(res)
