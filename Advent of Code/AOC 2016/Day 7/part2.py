with open("input.txt") as file:
    data = file.read()
    ips = data.splitlines()

res = 0

for ip in ips:
    is_hypernet = False
    supernet, hypernet = set(), set()

    for i in range(len(ip) - 2):
        if (ip[i] == "["):
            is_hypernet = True
        elif (ip[i] == "]"):
            is_hypernet = False
        
        if (ip[i] == ip[i + 2] and ip[i] != ip[i + 1]):
            if (is_hypernet):
                hypernet.add(ip[i:i + 3])
            else:
                supernet.add(ip[i:i + 3])
    
    for s in supernet:
        target = s[1] + s[0] + s[1]

        if (target in hypernet):
            res += 1
            break

print(res)
