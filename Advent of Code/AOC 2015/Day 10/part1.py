with open("input.txt") as file:
    data = file.read()
    sequence = data

for _ in range(40):
    new_sequence = []
    n = len(sequence)
    i = 0

    while (i < n):
        count = 0
        curr = sequence[i]

        while (i < n and sequence[i] == curr):
            count += 1
            i += 1
        
        new_sequence.append(str(count))
        new_sequence.append(curr)
    
    sequence = "".join(new_sequence)

res = len(sequence)
print(res)
