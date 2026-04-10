with open("input.txt") as file:
    data = file.read()
    codes = data.splitlines()

res = 0

for s in codes:
    n = len(s)
    res -= n
    count = 2

    for c in s:
        if (c == "\"" or c == "\\"):
            count += 1

        count += 1
    
    res += count

print(res)
