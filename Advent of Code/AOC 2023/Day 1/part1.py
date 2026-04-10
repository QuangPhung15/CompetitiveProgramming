with open("input.txt") as file:
    data = file.read()
    calibration = data.splitlines()

res = 0

for cali in calibration:
    first, last = "", ""

    for c in cali:
        if (not c.isdigit()):
            continue

        if (not first):
            first = c
        
        last = c
    
    res += int(first) * 10 + int(last)

print(res)
