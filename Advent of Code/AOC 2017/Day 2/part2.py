with open("input.txt") as file:
    data = file.read().splitlines()
    spreadsheet = [list(map(int, d.split())) for d in data]

res = 0

for s in spreadsheet:
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if (s[i] % s[j] == 0):
                res += s[i] // s[j]
            elif (s[j] % s[i] == 0):
                res += s[j] // s[i]

print(res)
