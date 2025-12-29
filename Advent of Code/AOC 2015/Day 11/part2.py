with open("input.txt") as file:
    data = file.read()
    password = data

times = 2
n = len(password)

def helper(s):
    has_consecutive = False
    seen = set()

    for i in range(len(s)):
        if (s[i] in ("i", "o", "l")):
            return False

        if (i + 2 < len(s) and ord(s[i + 1]) - ord(s[i]) == 1 and ord(s[i + 2]) - ord(s[i]) == 2):
            has_consecutive = True
        
        if (i + 1 < len(s) and s[i] == s[i + 1]):
            seen.add(s[i] + s[i + 1])
 
    return len(seen) >= 2 and has_consecutive

while (times):
    new_password = ""
    carry = 1

    for i in reversed(range(n)):
        new_password += chr((ord(password[i]) - ord("a") + carry) % 26 + ord("a"))
        carry = 0 if (password[i] <= new_password[-1]) else 1

    password = new_password[::-1]

    if (helper(password)):
        times -= 1

print(password)
