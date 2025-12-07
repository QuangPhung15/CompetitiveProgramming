with open("input.txt") as file:
    data = file.read()
    report = list(map(int, data.splitlines()))

res = 0
n = len(report)
report.sort()
i = 0

while (i < n - 2):
    l, r = i + 1, n - 1
    target = 2020 - report[i]

    while (l < r):
        if (report[l] + report[r] == target):
            res += report[i] * report[l] * report[r]
            l += 1
            r -= 1

            while (l < r and report[l] == report[l - 1]):
                l += 1
            
            while (l < r and report[r] == report[r + 1]):
                r -= 1
        elif (report[l] + report[r] < target):
            l += 1

            while (l < r and report[l] == report[l - 1]):
                l += 1
        else:
            r -= 1

            while (l < r and report[r] == report[r + 1]):
                r -= 1
    
    i += 1
    
    while (i < n - 2 and report[i] == report[i - 1]):
        i += 1

print(res)
