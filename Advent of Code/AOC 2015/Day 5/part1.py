with open("input.txt") as file:
    data = file.read()
    strings = data.splitlines()

res = 0
vowels = {"a", "e", "i", "o", "u"}
banned_words = {"ab", "cd", "pq", "xy"}

for s in strings:
    vowel_count = 0
    has_double = False
    has_banned_word = False

    for i in range(len(s) - 1):
        if (s[i] in vowels):
            vowel_count += 1
        
        if (s[i] == s[i + 1]):
            has_double = True
        
        if (s[i:i + 2] in banned_words):
            has_banned_word = True
    
    if (s[-1] in vowels):
        vowel_count += 1
    
    res += vowel_count >= 3 and has_double and not has_banned_word

print(res)
