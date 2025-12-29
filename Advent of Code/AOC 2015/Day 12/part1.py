with open("input.txt") as file:
    data = file.read()
    document = data

res = 0
n = len(document)
i = 0

while (i < n):
    if (document[i] == "-"):
        i += 1
        num = 0

        while (i < n and document[i].isdigit()):
            num = num * 10 + int(document[i])
            i += 1
        
        res -= num
    elif (document[i].isdigit()):
        num = 0

        while (i < n and document[i].isdigit()):
            num = num * 10 + int(document[i])
            i += 1
        
        res += num
    else:
        i += 1

print(res)
        