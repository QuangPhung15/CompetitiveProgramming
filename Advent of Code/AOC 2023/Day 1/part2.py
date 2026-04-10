with open("example2.txt") as file:
    data = file.read()
    calibration = data.splitlines()

res = 0
mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5", 
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

for cali in calibration:
    first, last = "", ""
    i = 0

    while (i < len(cali)):
        curr = ""

        if (cali[i].isdigit()):
            curr = cali[i]
        else:
            if (cali[i:i + 3] in mapping):
                curr = mapping[cali[i:i + 3]]
            elif (cali[i:i + 4] in mapping):
                curr = mapping[cali[i:i + 4]]
            elif (cali[i:i + 5] in mapping):
                curr = mapping[cali[i:i + 5]]
                 
        if (curr):
            if (not first):
                first = curr
            
            last = curr
        
        i += 1
    
    res += int(first) * 10 + int(last)

print(res)