with open("input.txt") as file:
    data = file.read().splitlines()
    rooms = []

    for d in data:
        line = d.split("-")
        names = line[:-1]
        sector_id, checksum = line[-1].split("[")
        rooms.append((names, int(sector_id), checksum[:-1]))

res = -1

for names, sector_id, checksum in rooms:
    shifts = sector_id % 26
    new_names = []

    for name in names:
        new_name = ""

        for n in name:
            new_name += chr(ord("a") + (ord(n) - ord("a") + shifts) % 26)

        new_names.append(new_name)

    code = " ".join(new_names)
    
    if (code == "northpole object storage"):
        res = sector_id
        break

print(res)
