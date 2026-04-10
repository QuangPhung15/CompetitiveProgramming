with open("input.txt") as file:
    data = file.read()
    stream = data

res = 0
stack = []
n = len(stream)
i = 0

while (i < n):
    if (stream[i] == "!"):
        i += 2
    elif (stack and stack[-1][1] == "<"):
        if (stream[i] == ">"):
            stack.pop()
        
        i += 1
    elif (stream[i] == "<"):
        stack.append((-1, stream[i]))
        i += 1
    elif (stream[i] == ">"):
        i += 1
    elif (stream[i] == "{"):
        if (stack):
            stack.append((stack[-1][0] + 1, stream[i]))
        else:
            stack.append((1, stream[i]))
        i += 1
    elif (stream[i] == "}"):
        if (stack and stack[-1][1] == "{"):
            res += stack.pop()[0]
            i += 1
    else:
        i += 1

print(res)
