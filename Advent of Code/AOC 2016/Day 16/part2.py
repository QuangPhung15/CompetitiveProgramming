with open("input.txt") as file:
    data = file.read()

target_length = 35651584
a = list(data) 

while (len(a) < target_length):
    b = []

    for c in reversed(a):
        if (c == "0"):
            b.append("1")
        else:
            b.append("0")
    
    a.append("0")
    a.extend(b)

a = a[:target_length]

while (len(a) % 2 == 0):
    temp = []

    for i in range(0, len(a), 2):
        if (a[i] == a[i + 1]):
            temp.append("1")
        else:
            temp.append("0")
    
    a = temp.copy()

res = "".join(a)
print(res)
