with open("input.txt") as file:
    data = file.read().splitlines()
    banks = data

res = 0

for b in banks:
    stack = []
    n = len(b)

    for i, c in enumerate(b):
        while (stack and c > stack[-1] and len(stack) + n - i > 12):
            stack.pop()

        stack.append(c)

        if (len(stack) > 12):
            stack.pop()

    joltages = int("".join(stack))
    res += joltages

print(res)
