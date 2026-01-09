with open("input.txt") as file:
    data = file.read()
    compressed_file = data

res = 0
n = len(compressed_file)
i = 0

def recursion():
    global i, n

    count = 0
    length, times = 0, 0

    i += 1

    while (i < n and compressed_file[i].isdigit()):
        length = length * 10 + int(compressed_file[i])
        i += 1
    
    i += 1

    while (i < n and compressed_file[i].isdigit()):
        times = times * 10 + int(compressed_file[i])
        i += 1
    
    i += 1
    l = i

    while (i - l < length):
        if (compressed_file[i] == "("):
            count += recursion()
        else:
            count += 1
            i += 1

    return count * times

while (i < n):
    if (compressed_file[i] == "("):
        res += recursion()
    else:
        res += 1
        i += 1

print(res)
