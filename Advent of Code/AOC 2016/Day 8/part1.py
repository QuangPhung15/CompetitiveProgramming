with open("input.txt") as file:
    data = file.read().splitlines()
    instructions = []

    for d in data:
        line = d.split()

        if (line[0] == "rect"):
            a, b = map(int, line[1].split("x"))
            instructions.append((line[0], a, b))
        else:
            instructions.append((line[0], line[1], int(line[2][2:]), int(line[4])))

res = 0
m, n = 6, 50
screen = [["."] * n for _ in range(m)]

def rotate_row(r, s):
    new_row = [""] * n

    for i in range(n):
        new_row[(i + s) % n] = screen[r][i]
    
    for i in range(n):
        screen[r][i] = new_row[i]

def rotate_col(c, s):
    new_col= [""] * m

    for i in range(m):
        new_col[(i + s) % m] = screen[i][c]
    
    for i in range(m):
        screen[i][c] = new_col[i]

for instruction in instructions:
    if (instruction[0] == "rect"):
        rows, cols = instruction[2], instruction[1]

        for i in range(rows):
            for j in range(cols):
                screen[i][j] = "#"
    else:
        if (instruction[1] == "row"):
            r, shifts = instruction[2], instruction[3]
            rotate_row(r, shifts)
        else:
            c, shifts = instruction[2], instruction[3]
            rotate_col(c, shifts)

for i in range(m):
    for j in range(n):
        res += 1 if (screen[i][j] == "#") else 0

print(res)
