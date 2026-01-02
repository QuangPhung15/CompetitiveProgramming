with open("input.txt") as file:
    data = file.read()
    instructions = data.splitlines()

res = ""
dirs = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}
r, c = 2, 0
keypad = [
    "  1  ",
    " 234 ",
    "56789",
    " ABC ",
    "  D  ",
]

for instruction in instructions:
    for i in instruction:
        dr, dc = dirs[i]
        newR, newC = r + dr, c + dc
    
        if (0 <= newR <= 4 and 0 <= newC <= 4 and keypad[newR][newC] != " "):
            r, c = newR, newC

    res += keypad[r][c]

print(res)
