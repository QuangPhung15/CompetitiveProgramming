with open("input.txt") as file:
    data = file.read()
    row, col = map(int, data.split())

res = 20151125
m, d = 252533, 33554393
r, c = 1, 1
i = 1

while (r != row or c != col):
    r -= 1
    c += 1

    if (r == 0):
        i += 1
        r, c = i, 1
    
    res = (res * m) % d

print(res)
