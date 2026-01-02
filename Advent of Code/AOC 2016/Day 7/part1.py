with open("input.txt") as file:
    data = file.read()
    ips = data.splitlines()

res = 0

for ip in ips:
    is_hypernet = False
    count_supernet, count_hypernet = 0, 0

    for i in range(len(ip) - 3):
        if (ip[i] == "["):
            is_hypernet = True
        elif (ip[i] == "]"):
            is_hypernet = False
        
        if (ip[i] == ip[i + 3] and ip[i + 1] == ip[i + 2] and ip[i] != ip[i + 1]):
            if (is_hypernet):
                count_hypernet += 1
            else:
                count_supernet += 1
    
    if (count_hypernet == 0 and count_supernet > 0):
        res += 1

print(res)
