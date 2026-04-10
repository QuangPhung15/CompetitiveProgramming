import hashlib

with open("input.txt") as file:
    data = file.read()
    secret_key = data

res = [""] * 8
curr = 1
count = 0

while (count < 8):
    input_str = secret_key + str(curr)
    output_str = hashlib.md5(input_str.encode("utf-8")).hexdigest()

    if (output_str[:5] == "00000"):
        i = output_str[5]

        if (i.isdigit() and 0 <= int(i) < 8 and res[int(i)] == ""):
            res[int(i)] = output_str[6]
            count += 1
    
    curr += 1

print("".join(res))
