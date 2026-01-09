with open("input.txt") as file:
    data = file.read()
    compressed_file = data

res = 0
n = len(compressed_file)
i = 0

while (i < n):
    if (compressed_file[i] == "("):
        length, times = 0, 0
        i += 1

        while (i < n and compressed_file[i].isdigit()):
            length = length * 10 + int(compressed_file[i])
            i += 1
        
        i += 1

        while (i < n and compressed_file[i].isdigit()):
            times = times * 10 + int(compressed_file[i])
            i += 1

        res += length * times
        i += length
    else:
        res += 1
    
    i += 1

print(res)
