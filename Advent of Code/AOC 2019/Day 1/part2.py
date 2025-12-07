with open("input.txt") as file:
    data = file.read()
    mass = list(map(int, data.splitlines()))

res = 0

def helper(fuel):
    count = 0

    while (fuel > 0):
        count += fuel
        fuel = fuel // 3 - 2
    
    return count

for m in mass:
    fuel = m // 3 - 2
    res += helper(fuel)

print(res)
