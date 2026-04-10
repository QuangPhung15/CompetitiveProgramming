import hashlib

with open("input.txt") as file:
    data = file.read()
    secret_key = data

res = ""
curr = 1

while (len(res) < 8):
    input_str = secret_key + str(curr)
    output_str = hashlib.md5(input_str.encode("utf-8")).hexdigest()

    if (output_str[:5] == "00000"):
        res += output_str[5]
    
    curr += 1

print(res)
