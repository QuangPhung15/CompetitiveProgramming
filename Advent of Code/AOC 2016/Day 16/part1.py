with open("input.txt") as file:
    data = file.read()

target_length = 272
a = data 

while (len(a) < target_length):
    b = a[::-1]
    temp = ""

    for c in b:
        if (c == "0"):
            temp += "1"
        else:
            temp += "0"
    
    b = temp
    a = a + "0" + b

a = a[:target_length]

while (len(a) % 2 == 0):
    temp = ""

    for i in range(0, len(a), 2):
        if (a[i] == a[i + 1]):
            temp += "1"
        else:
            temp += "0"
    
    a = temp

res = a
print(res)
