class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        n = len(s)
        mapping = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        i = 0

        while (i < n):
            if (i + 1 < n and s[i:i + 2] in mapping):
                res += mapping[s[i:i + 2]]
                i += 2
            else:
                res += mapping[s[i]]
                i += 1

        return res

"""
Time Complexity: O(N)
Space Complexity: O(1)

Where 
N = length of string s
"""