with open("input.txt") as file:
    data = file.read().splitlines()
    ranges = data[0].split(",")

res = 0

for r in ranges:
    s, e = map(int, r.split("-"))

    for i in range(s, e + 1):
        num = str(i)
        n = len(num)

        if (n % 2 == 0 and num[:n // 2] == num[n // 2:]):
            res += i

print(res)
