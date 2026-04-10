import hashlib

with open("input.txt") as file:
    data = file.read()
    secret_key = data

res = 1

while (True):
    input_str = secret_key + str(res)
    output_str = hashlib.md5(input_str.encode("utf-8")).hexdigest()

    if (output_str[:6] == "000000"):
        break

    res += 1

print(res)
