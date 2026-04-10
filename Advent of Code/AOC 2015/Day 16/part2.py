with open("input.txt") as file:
    data = file.read().splitlines()
    gifts = []

    for d in data:
        line = d.split()
        gifts.append(
            (
                int(line[1][:-1]), 
                {
                    line[2][:-1]: int(line[3][:-1]),
                    line[4][:-1]: int(line[5][:-1]),
                    line[6][:-1]: int(line[7])
                }
            )
        )

ticker_tap = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
GREATER_THAN = {"cats", "trees"}
LESS_THAN = {"pomeranians", "goldfish"}

def helper(properties):
    for k, v in properties.items():
        target = ticker_tap[k]

        if (k in GREATER_THAN and v <= target):
            return False
        if (k in LESS_THAN and v >= target):
            return False
        if (k not in GREATER_THAN | LESS_THAN and v != target):
            return False

    return True

res = next(
    i for i, props in gifts if (helper(props))
)

print(res)