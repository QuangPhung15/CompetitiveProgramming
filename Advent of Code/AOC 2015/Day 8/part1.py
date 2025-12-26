with open("input.txt") as file:
    data = file.read()
    codes = data.splitlines()

res = 0

for c in codes:
    n = len(c)
    res += n
    count = 0
    i = 1

    while (i < n - 1):
        count += 1

        if (c[i] == "\\" and c[i + 1] == "x"):
            i += 4
        elif (c[i] == "\\" and c[i + 1] != "x"):
            i += 2
        else:
            i += 1
    
    res -= count

print(res)
