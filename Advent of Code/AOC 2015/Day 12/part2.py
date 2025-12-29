with open("input.txt") as file:
    data = file.read()
    document = data

n = len(document)
i = 0

def recursive():
    global i

    has_red = False
    total = 0

    while (i < n):
        if (document[i] == "{" or document[i] == "["):
            i += 1
            total += recursive()
        elif (document[i] == "}" or document[i] == "]"):
            i += 1
            return 0 if (has_red and document[i - 1] == "}") else total
        elif (document[i] == "-"):
            i += 1
            num = 0

            while (i < n and document[i].isdigit()):
                num = num * 10 + int(document[i])
                i += 1
            
            total -= num
        elif (document[i].isdigit()):
            num = 0

            while (i < n and document[i].isdigit()):
                num = num * 10 + int(document[i])
                i += 1
            
            total += num
        elif (i + 2 < n and document[i:i + 3] == "red"):
            has_red = True
            i += 3
        else:
            i += 1
    
    return total

res = recursive()
print(res)
